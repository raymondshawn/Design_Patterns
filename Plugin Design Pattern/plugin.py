class PaymentGateway:
    def process_payment(self, amount):
        raise NotImplementedError

class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} via PayPal.")

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing payment of {amount} via Stripe.")

class PaymentProcessor:
    def __init__(self):
        self.gateway = None

    def set_gateway(self, gateway):
        self.gateway = gateway

    def process_payment(self, amount):
        if self.gateway is None:
            print("No payment gateway set.")
        else:
            self.gateway.process_payment(amount)

# Usage
processor = PaymentProcessor()

# PayPal payment
processor.set_gateway(PayPalGateway())
processor.process_payment(100)

# Stripe payment
processor.set_gateway(StripeGateway())
processor.process_payment(200)
