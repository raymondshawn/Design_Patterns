"""class PaymentGateway:
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
"""


class PaymentGateway:
    """process payment by each gateway
    """

    def process_payment(self, amount):
        raise NotImplementedError("Implenment the method")


class PayPalGateway(PaymentGateway):
    """process payment via paypal


    """

    def process_payment(self, amount):
        print(f"Processing payment of {amount} via PayPal.")


class StripeGateway(PaymentGateway):
    """process payment via stripe


    """

    def process_payment(self, amount):
        print(f"Processing payment of {amount} via Stripe.")


class PaymentProcessor:
    """Payment processor which adds a gateway/gateways to its list of gateway to use and selects the one to use in the set gateway method
    """

    def __init__(self):
        self.gateways = []
        self.gateway = None

    def add_gateway(self, gateway):
        self.gateways.append(gateway)

    def add_gateways(self, gateways):
        self.gateways.extend(gateways)

    def set_gateway(self, gateway):
        self.gateway = gateway

    def process_payment(self, amount):
        if self.gateway is None:
            print("No payment gateway set.")
        else:
            self.gateway.process_payment(amount)


# Usage
processor = PaymentProcessor()
paypal_gateway = PayPalGateway()
stripe_gateway = StripeGateway()
gateways = [paypal_gateway, stripe_gateway]

processor.add_gateways(gateways)
# PayPal payment
processor.set_gateway(paypal_gateway)
processor.process_payment(100)

# Stripe payment
processor.set_gateway(stripe_gateway)
processor.process_payment(200)
