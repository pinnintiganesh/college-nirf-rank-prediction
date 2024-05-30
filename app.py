from flask import Flask, render_template, request
import joblib



# # Load the trained model
model = joblib.load('college_rank_predictor.pkl')




from flask import Flask, render_template, request
import plotly.graph_objects as got
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

app = Flask(__name__)

# Sample data (replace this with your actual data)
# Features of the top-ranked college
df=pd.read_csv("./dataset/engineering.csv")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user-entered features
        user_features = {}
        rank_to_access = request.form.get("rta",None)
        tlr = float(request.form.get("tlr"))
        rpc = float(request.form.get("rpc"))
        go = float(request.form.get("go"))
        oi = float(request.form.get("oi"))
        perception = float(request.form.get("perception"))
        
        for i in [tlr, rpc, go, oi, perception]:
            if not 0<i<=100:
                return render_template('index1.html',message=f"Entered values must be from 1 to 100." )
        prediction = model.predict([[tlr, rpc, go, oi, perception]])
        prediction = prediction -1
        if rank_to_access=='':
            return render_template('index1.html',prediction=int(prediction[0].round()))
        row = df.loc[df['rank'] == int(rank_to_access)]
        if row.empty:
            return render_template('index1.html',message="Entered rank is invalid")
    
        top_college_features = {}
        for column in row.columns:
            # Exclude the 'Rank' column
            if column in ['tlr', 'rpc', 'go', 'oi', 'perception']:
                top_college_features[column] = row.iloc[0][column]
        print(top_college_features)


        for feature in top_college_features.keys():
            user_features[feature] = float(request.form[feature])
        
        # Calculate differences in features
        differences = {feature: user_features[feature] - top_college_features[feature] for feature in top_college_features}
        difference_count = sum(1 for diff in differences.values() if diff != 0)
        
        

        plot_filenames = []
        for feature, value in user_features.items():
            fig = got.Figure()

            # Add features of top-ranked college
            fig.add_trace(got.Bar(
                x=[feature],
                y=[top_college_features[feature]],
                name='Top College',
                marker_color='blue'
            ))

            # Add features of user-entered college
            fig.add_trace(got.Bar(
                x=[feature],
                y=[value],
                name='Your College',
                marker_color='orange'
            ))

            # Add differences
            bar_color = 'green' if differences[feature] > 0 else 'red'
            fig.add_trace(got.Bar(
                x=[feature],
                y=[differences[feature]],
                name='Differences',
                marker_color=bar_color
            ))

            # Update layout
            fig.update_layout(
                title=f'Comparison of {feature} with Top-Ranked College',
                xaxis_title='Features',
                yaxis_title='Values / Differences',
                barmode='group'
            )

            # Save plot as HTML file
            plot_filename = f"plot_{feature}.html"
            plot_filenames.append(plot_filename)
            fig.write_html(f"static/{plot_filename}")







        
        # Create Plotly chart
        fig = got.Figure()

        # Add features of top-ranked college
        fig.add_trace(got.Bar(
            x=list(top_college_features.keys()),
            y=list(top_college_features.values()),
            name='Top College',
            marker_color='blue'
        ))

        # Add features of user-entered college
        fig.add_trace(got.Bar(
            x=list(user_features.keys()),
            y=list(user_features.values()),
            name='Your College',
            marker_color='orange'
        ))

        # Add differences
        bar_colors = ['green' if diff > 0 else 'red' for diff in differences.values()]
        fig.add_trace(got.Bar(
            x=list(differences.keys()),
            y=list(differences.values()),
            name='Differences',
            marker_color=bar_colors
        ))

        # Update layout
        fig.update_layout(
            title='Comparison of Feature Values with Top-Ranked College',
            xaxis_title='Features',
            yaxis_title='Values / Differences',
            barmode='group'
        )
        
        

        # Convert Plotly chart to HTML
        chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        # print(prediction)
        return render_template('index1.html',chart_html=chart_html, plot_filenames=plot_filenames, prediction=int(prediction[0].round()))
        

    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
