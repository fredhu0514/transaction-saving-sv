from .template import TemplateCard

class DiscoverItCashBack(TemplateCard):
    @classmethod
    def get_top_deals(cls, quarterly_special_usage, amount, coupons):
        general_coupon = coupons.pop(0)
        special_coupons = coupons
        result = []

        result.append({
            "special_usage": 0.000,
            "special_cash_back": 0.000,
            "general_usage": amount,
            "general_cash_back": general_coupon["rate"] * amount,
            "coupon": general_coupon
        })
        
        for coupon in special_coupons:
            if quarterly_special_usage >= coupon["upper_limit"]:
                continue
            special_usage = min(amount, coupon["upper_limit"] - quarterly_special_usage)
            special_cash_back = special_usage * coupon["rate"]
            general_usage = amount - special_usage
            general_cash_back = general_usage * general_coupon["rate"]
            result.append({
                "special_usage": special_usage,
                "special_cash_back": special_cash_back,
                "general_usage": general_usage,
                "general_cash_back": general_cash_back,
                "coupon": coupon
            })
            result.sort(key=lambda x: -(x["special_cash_back"] + x["general_cash_back"]))
            result = result if len(result) < 4 else result[:3] # Get first 3 items
            return result