from flask import Flask

from random_data_generator.peer_payouts.payments import PayoutProvider

app = Flask(__name__)


@app.route("/payout-provider")
def single_payout_generator():
    payout_provider = PayoutProvider()
    json_response = payout_provider.create_payout().json()
    return json_response, 200, {"Content-Type": "application/json"}
