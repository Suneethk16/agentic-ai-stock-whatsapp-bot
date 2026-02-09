class TrendAgent:
    def calculate_trend(self, data, days):
        """
        Calculate price trend over a given number of days.
        Returns a clean dictionary with Python floats (no NumPy types).
        """

        if data is None or len(data) < days:
            return None

        # Select last N days
        recent_data = data.tail(days)

        # Convert NumPy types to Python floats
        start_price = float(recent_data.iloc[0]["Close"])
        end_price = float(recent_data.iloc[-1]["Close"])

        # Percentage change
        percent_change = ((end_price - start_price) / start_price) * 100
        percent_change = float(percent_change)

        # Trend classification
        if percent_change > 2:
            trend_label = "Uptrend 📈"
        elif percent_change < -2:
            trend_label = "Downtrend 📉"
        else:
            trend_label = "Sideways ⚖️"

        return {
            "days": days,
            "start_price": round(start_price, 2),
            "end_price": round(end_price, 2),
            "percent_change": round(percent_change, 2),
            "trend": trend_label
        }

    def run(self, hist_data):
        """
        Analyze short-term, mid-term, and long-term trends.
        """

        print("\n📈 Performing historical trend analysis...\n")

        trends = {
            "7_days": self.calculate_trend(hist_data, 7),
            "30_days": self.calculate_trend(hist_data, 30),
            "90_days": self.calculate_trend(hist_data, 90),
        }

        return trends
