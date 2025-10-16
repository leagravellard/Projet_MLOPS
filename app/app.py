from flask import Flask, render_template, request
import joblib
import pandas as pd

# ======================================================
# 🔧 Initialisation de l'application Flask
# ======================================================
app = Flask(__name__)

# Chargement du modèle final (ML2 : Régression Logistique)
model = joblib.load("model_ML2.pkl")


# ======================================================
# 🔮 Fonction de prédiction
# ======================================================
def predict_default(features):
    """Prend un dictionnaire de caractéristiques et renvoie 0 (pas de défaut) ou 1 (défaut)"""
    data = pd.DataFrame([features])
    prediction = model.predict(data)
    return int(prediction[0])


# ======================================================
# 🏠 Page d'accueil
# ======================================================
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ======================================================
# 📊 Route de prédiction
# ======================================================
@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        try:
            features = {
                "credit_lines_outstanding": int(
                    request.form["credit_lines_outstanding"]
                ),
                "loan_amt_outstanding": float(request.form["loan_amt_outstanding"]),
                "total_debt_outstanding": float(request.form["total_debt_outstanding"]),
                "income": float(request.form["income"]),
                "years_employed": int(request.form["years_employed"]),
                "fico_score": int(request.form["fico_score"]),
            }

            prediction = predict_default(features)

            if prediction == 1:
                result = "⚠️ Risque élevé de défaut de paiement !"
                color = "danger"
            else:
                result = "✅ Aucun risque de défaut détecté."
                color = "success"

            return render_template("index.html", prediction_text=result, color=color)

        except Exception as e:
            return render_template(
                "index.html", prediction_text=f"Erreur : {e}", color="warning"
            )


# ======================================================
# 🚀 Lancement de l'application
# ======================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
