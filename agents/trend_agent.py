class TrendAgent:
    def calculate_trend(self, data, days):
        if len(data) < days:
            return None

        recent_data = data.tail(days)
        start_price = recent_data.iloc[0]["Close"]
        end_price = recent_data.iloc[-1]["Close"]

        percent_change = ((end_price - start_price) / start_price) * 100

        if percent_change > 2:
            trend = "Uptrend 📈"
        elif percent_change < -2:
            trend = "Downtrend 📉"
        else:
            trend = "Sideways ⚖️"

        return {
            "days": days,
            "start_price": round(start_price, 2),
            "end_price": round(end_price, 2),
            "percent_change": round(percent_change, 2),
            "trend": trend
        }

    def run(self, hist_data):
        print("\n📈 Performing historical trend analysis...\n")

        trends = {
            "7_days": self.calculate_trend(hist_data, 7),
            "30_days": self.calculate_trend(hist_data, 30),
            "90_days": self.calculate_trend(hist_data, 90),
        }

        return trends
