# MediReach AI
**Smart Preventive Healthcare for Underserved Communities**

A student prototype built with Python, Streamlit, Pandas, and unit tests. It demonstrates a simple flow: input sample vitals and symptoms → transparent rule-based screening flag → preventive guidance/referral prompt.

## Important safety note
This is an educational demonstration, **not a medical device or diagnostic tool**. The rules are illustrative and have not been clinically validated. Do not use it to make medical decisions, and do not enter identifiable or real patient information. A low flag does not mean a person is healthy. Urgent or worsening symptoms require professional assessment/emergency help.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Deploy for a public demo
1. Upload this folder to a GitHub repository.
2. Open [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in with GitHub and choose **Create app**.
4. Select your repository, branch (`main`), and main file path (`app.py`).
5. Deploy, then copy the public app URL into your presentation/form.

## Repository contents
- `app.py` — Streamlit interface
- `screening.py` — demo rule engine and simulated examples
- `tests/test_screening.py` — automated unit tests
- `requirements.txt` — Python dependencies

## Data and privacy
All example cases are simulated. This demo does not connect to health records, devices, hospitals, or telemedicine services, and does not intentionally save submitted form values.
