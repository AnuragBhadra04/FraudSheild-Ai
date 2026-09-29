import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #0b1120;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.hero {
    padding: 35px;
    border-radius: 22px;
    background: linear-gradient(
        135deg,
        #111827,
        #1d4ed8
    );
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    color: #dbeafe;
}

.card {
    background: #111827;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #1f2937;
    margin-bottom: 20px;
}

.metric {
    background: #111827;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #1f2937;
}

.metric-title {
    color: #94a3b8;
    font-size: 14px;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    margin-top: 5px;
}

.fraud-box {
    padding: 30px;
    border-radius: 18px;
    background: #3f1515;
    border: 1px solid #ef4444;
    text-align: center;
}

.safe-box {
    padding: 30px;
    border-radius: 18px;
    background: #063b2b;
    border: 1px solid #10b981;
    text-align: center;
}

.info-box {
    padding: 20px;
    border-radius: 15px;
    background: #172554;
    border: 1px solid #2563eb;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    bundle = joblib.load(
        "fraud_detection_model.pkl"
    )

    return bundle


try:

    bundle = load_model()

    model = bundle["model"]

    amount_scaler = bundle["amount_scaler"]

    time_scaler = bundle["time_scaler"]

    selected_features = bundle["selected_features"]

    threshold = bundle["threshold"]

except Exception as e:

    st.error(
        "❌ Could not load fraud_detection_model.pkl"
    )

    st.code(str(e))

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🛡️ FraudShield AI")

    st.markdown("---")

    st.markdown("### Model")

    st.write("Random Forest")

    st.write(
        f"Features: {len(selected_features)}"
    )

    st.write(
        f"Threshold: {threshold}"
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🔍 Single Transaction",
            "📂 Batch Prediction",
            "ℹ️ About"
        ]
    )

    st.markdown("---")

    st.caption(
        "Credit Card Fraud Detection"
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.markdown(
    '''
    <div class="hero">
        <div style="font-size:42px;font-weight:800;">
            🛡️ FraudShield AI
        </div>
        <div style="font-size:18px;margin-top:8px;color:#dbeafe;">
            Intelligent Credit Card Fraud Detection using Machine Learning
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown("""
        <div class="metric">

        <div class="metric-title">
        MODEL
        </div>

        <div class="metric-value">
        Random Forest
        </div>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="metric">

        <div class="metric-title">
        FEATURES
        </div>

        <div class="metric-value">
        30
        </div>

        </div>
        """, unsafe_allow_html=True)


    with col3:

        st.markdown("""
        <div class="metric">

        <div class="metric-title">
        THRESHOLD
        </div>

        <div class="metric-value">
        0.50
        </div>

        </div>
        """, unsafe_allow_html=True)


    with col4:

        st.markdown("""
        <div class="metric">

        <div class="metric-title">
        STATUS
        </div>

        <div class="metric-value">
        🟢 LIVE
        </div>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("")


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("""
        <div class="card">

        <h2>🔍 Single Transaction</h2>

        <p>
        Enter transaction information and allow the
        Random Forest model to estimate the probability
        of fraud.
        </p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="card">

        <h2>📂 Batch Analysis</h2>

        <p>
        Upload multiple transactions through a CSV file
        and analyze them together.
        </p>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">

    <h3>⚙️ Machine Learning Pipeline</h3>

    Transaction Data
    → Preprocessing
    → Feature Transformation
    → Random Forest
    → Fraud Probability
    → Final Prediction

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SINGLE TRANSACTION
# ============================================================

elif page == "🔍 Single Transaction":

    st.markdown("""
    <div class="hero">

        <h1>🔍 Transaction Analysis</h1>

        <p>
        Analyze an individual credit card transaction
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">

    Enter the transaction values below.
    The application automatically calculates
    scaled_amount and scaled_time.

    </div>
    """, unsafe_allow_html=True)


    st.markdown("### Transaction Information")


    # --------------------------------------------------------
    # TIME AND AMOUNT
    # --------------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        transaction_time = st.number_input(
            "Transaction Time",
            value=0.0,
            format="%.6f"
        )


    with col2:

        transaction_amount = st.number_input(
            "Transaction Amount",
            min_value=0.0,
            value=100.0,
            format="%.2f"
        )


    st.markdown("---")

    st.markdown("### PCA Features")

    st.caption(
        "Enter V1 to V28 values."
    )


    # --------------------------------------------------------
    # V1 - V28
    # --------------------------------------------------------

    v_values = {}

    cols = st.columns(4)


    for i in range(1, 29):

        with cols[(i - 1) % 4]:

            v_values[f"V{i}"] = st.number_input(
                f"V{i}",
                value=0.0,
                format="%.6f",
                key=f"single_v{i}"
            )


    st.markdown("")


    # --------------------------------------------------------
    # PREDICT
    # --------------------------------------------------------

    if st.button(
        "🚀 Analyze Transaction",
        use_container_width=True
    ):

        try:

            # ================================================
            # SCALE AMOUNT
            # ================================================

            scaled_amount = amount_scaler.transform(
                [[transaction_amount]]
            )[0][0]


            # ================================================
            # SCALE TIME
            # ================================================

            scaled_time = time_scaler.transform(
                [[transaction_time]]
            )[0][0]


            # ================================================
            # CREATE MODEL INPUT
            # ================================================

            input_data = {}

            for i in range(1, 29):

                input_data[f"V{i}"] = v_values[f"V{i}"]


            input_data["scaled_amount"] = scaled_amount

            input_data["scaled_time"] = scaled_time


            input_df = pd.DataFrame(
                [input_data]
            )


            # ================================================
            # EXACT FEATURE ORDER
            # ================================================

            input_df = input_df[
                selected_features
            ]


            # ================================================
            # PREDICTION
            # ================================================

            prediction = model.predict(
                input_df
            )[0]


            probability = model.predict_proba(
                input_df
            )[0][1]


            # ================================================
            # RESULT
            # ================================================

            st.markdown("---")

            if prediction == 1:

                st.markdown(f"""
                <div class="fraud-box">

                <h1>🚨 FRAUD DETECTED</h1>

                <h2>
                Potentially Fraudulent Transaction
                </h2>

                <p>
                Fraud Probability:
                <b>{probability * 100:.2f}%</b>
                </p>

                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown(f"""
                <div class="safe-box">

                <h1>✅ LEGITIMATE</h1>

                <h2>
                Transaction Appears Legitimate
                </h2>

                <p>
                Fraud Probability:
                <b>{probability * 100:.2f}%</b>
                </p>

                </div>
                """, unsafe_allow_html=True)


            st.markdown("### Fraud Probability")

            st.progress(
                float(probability)
            )


            col1, col2 = st.columns(2)


            with col1:

                st.metric(
                    "Fraud Probability",
                    f"{probability * 100:.2f}%"
                )


            with col2:

                st.metric(
                    "Classification",
                    "FRAUD"
                    if prediction == 1
                    else "LEGITIMATE"
                )


        except Exception as e:

            st.error(
                "Prediction failed."
            )

            st.exception(e)


# ============================================================
# BATCH PREDICTION
# ============================================================

elif page == "📂 Batch Prediction":

    st.markdown("""
    <div class="hero">

        <h1>📂 Batch Fraud Detection</h1>

        <p>
        Analyze multiple transactions simultaneously
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="info-box">

    Upload a CSV containing:

    <br><br>

    <b>
    Time, V1-V28, Amount
    </b>

    <br><br>

    The application will automatically generate
    scaled_amount and scaled_time.

    </div>
    """, unsafe_allow_html=True)


    uploaded_file = st.file_uploader(
        "Upload Transaction CSV",
        type=["csv"]
    )


    if uploaded_file is not None:

        try:

            df = pd.read_csv(
                uploaded_file
            )


            st.markdown("### Uploaded Data")

            st.dataframe(
                df.head(10),
                use_container_width=True
            )


            required_columns = [
                "Time"
            ] + [
                f"V{i}" for i in range(1, 29)
            ] + [
                "Amount"
            ]


            missing_columns = [
                col
                for col in required_columns
                if col not in df.columns
            ]


            if missing_columns:

                st.error(
                    "Missing required columns:"
                )

                st.write(
                    missing_columns
                )


            else:

                if st.button(
                    "🚀 Run Fraud Detection",
                    use_container_width=True
                ):

                    # ========================================
                    # SCALE AMOUNT
                    # ========================================

                    df["scaled_amount"] = (
                        amount_scaler.transform(
                            df[["Amount"]]
                        )
                    )


                    # ========================================
                    # SCALE TIME
                    # ========================================

                    df["scaled_time"] = (
                        time_scaler.transform(
                            df[["Time"]]
                        )
                    )


                    # ========================================
                    # MODEL INPUT
                    # ========================================

                    model_input = df[
                        selected_features
                    ]


                    # ========================================
                    # PREDICTIONS
                    # ========================================

                    predictions = model.predict(
                        model_input
                    )


                    probabilities = model.predict_proba(
                        model_input
                    )[:, 1]


                    # ========================================
                    # RESULTS
                    # ========================================

                    result_df = df.copy()


                    result_df[
                        "Fraud Probability"
                    ] = probabilities


                    result_df[
                        "Prediction"
                    ] = np.where(
                        predictions == 1,
                        "Fraud",
                        "Legitimate"
                    )


                    # ========================================
                    # SUMMARY
                    # ========================================

                    total = len(
                        result_df
                    )

                    fraud_count = int(
                        (predictions == 1).sum()
                    )

                    legitimate_count = (
                        total - fraud_count
                    )


                    st.success(
                        "✅ Analysis completed!"
                    )


                    col1, col2, col3 = st.columns(3)


                    with col1:

                        st.metric(
                            "Total Transactions",
                            total
                        )


                    with col2:

                        st.metric(
                            "Potential Fraud",
                            fraud_count
                        )


                    with col3:

                        st.metric(
                            "Legitimate",
                            legitimate_count
                        )


                    st.markdown(
                        "### Prediction Results"
                    )


                    st.dataframe(
                        result_df[
                            [
                                "Time",
                                "Amount",
                                "Fraud Probability",
                                "Prediction"
                            ]
                        ],
                        use_container_width=True
                    )


                    # ========================================
                    # DOWNLOAD
                    # ========================================

                    csv = result_df.to_csv(
                        index=False
                    )


                    st.download_button(
                        "⬇️ Download Prediction Results",
                        csv,
                        "fraud_predictions.csv",
                        "text/csv",
                        use_container_width=True
                    )


        except Exception as e:

            st.error(
                "Could not process the CSV."
            )

            st.exception(e)


# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.markdown("""
    <div class="hero">

        <h1>ℹ️ About FraudShield AI</h1>

        <p>
        Machine Learning based Credit Card Fraud Detection
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("""
    <div class="card">

    <h2>Project Overview</h2>

    <p>
    FraudShield AI is a machine learning based system
    designed to identify potentially fraudulent credit
    card transactions.
    </p>

    <h3>Machine Learning Model</h3>

    <p>
    Random Forest Classifier
    </p>

    <h3>Input Features</h3>

    <p>
    V1 - V28, Transaction Time and Transaction Amount
    </p>

    <h3>Preprocessing</h3>

    <p>
    StandardScaler is used to transform transaction
    Amount and Time into scaled_amount and scaled_time.
    </p>

    <h3>Prediction</h3>

    <p>
    The Random Forest model produces a fraud probability
    and classification.
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("### Model Features")

    feature_df = pd.DataFrame({
        "Feature": selected_features
    })

    st.dataframe(
        feature_df,
        use_container_width=True
    )