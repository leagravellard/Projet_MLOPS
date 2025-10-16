import joblib
import pandas as pd

# ============================================================
# 🧠 Chargement du modèle ML2 (Régression Logistique)
# ============================================================
model = joblib.load("app/model_ML2.pkl")

# ============================================================
# 🔹 Exemple de données d'entrée (sans customer_id)
# ============================================================
test_input = {
    "credit_lines_outstanding": [0],
    "loan_amt_outstanding": [5221.545193],
    "total_debt_outstanding": [3915.471226],
    "income": [78039.38546],
    "years_employed": [5],
    "fico_score": [605]
}

X_test = pd.DataFrame(test_input)

# ============================================================
# ✅ Test de prédiction
# ============================================================
def test_predict_default():
    """Vérifie que la prédiction du modèle est correcte et égale à 0 (pas de défaut)."""
    prediction = model.predict(X_test)[0]
    print(f"🔍 Prédiction du modèle ML2 : {prediction}")

    # Vérifie que la prédiction est bien binaire (0 ou 1)
    assert prediction in [0, 1], "❌ La prédiction n'est pas binaire (0 ou 1)."

    # Vérifie que le modèle prédit bien 0 (aucun défaut de paiement attendu)
    assert prediction == 0, f"❌ Le modèle a prédit {prediction}, alors qu'on attendait 0."

    print("✅ Test réussi : le modèle prédit correctement 0 (aucun défaut de paiement).")


# ============================================================
# 🚀 Exécution directe du test
# ============================================================
if __name__ == "__main__":
    test_predict_default()
