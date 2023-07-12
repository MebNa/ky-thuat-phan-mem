from flask import Flask, jsonify, request
import movie_recommend

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    title = request.args.get('title')
    if title is None:
        return jsonify({"error": "Missing 'title' parameter"}), 400

    recommendations = movie_recommend.get_recommendations(title)
    if recommendations is None:
        return jsonify({"error": "Title not found"}), 404

    return jsonify(recommendations.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)