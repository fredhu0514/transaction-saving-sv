class TemplateCard:
    @classmethod
    def get_top_deal(coupon_cycle_usage, amount, coupons):
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
            # Pick the higher lower limit
            dynamic_lower_limit = max(coupon_cycle_usage, coupon["lower_limit"])
            # In case the dynamic lower limit has already passed upper limit, then the range will be 0.
            if dynamic_lower_limit >= coupon["upper_limit"]:
                # If the dynamic_lower_limit reaches or beyonds coupon["upper_limit"], no range is effective for coupon.
                # Continue because the result will be the same as the general coupon applied to all amount.
                continue
            # The amount that over the dynamic lower limit
            over_lower_limit_amount = max(coupon_cycle_usage + amount - dynamic_lower_limit, 0.000)
            # Maximum effective amount can only be the effective range's width.
            special_usage = min(over_lower_limit_amount, coupon["upper_limit"] - dynamic_lower_limit)
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