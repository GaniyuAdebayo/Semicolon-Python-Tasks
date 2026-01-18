def riderPay(no_of_successful_deliveries):

	if not isinstance(no_of_successful_deliveries, int) or no_of_successful_deliveries < 0:

		return "Invalid input"

	match (no_of_successful_deliveries):

		case no_of_successful_deliveries if no_of_successful_deliveries >= 70:
			return no_of_successful_deliveries * 500 + 5000

		case no_of_successful_deliveries if no_of_successful_deliveries >= 60:
			return no_of_successful_deliveries * 250 + 5000

		case no_of_successful_deliveries if no_of_successful_deliveries >= 50:
			return no_of_successful_deliveries * 200 + 5000

		case _:
			return no_of_successful_deliveries * 160 + 5000