# --- H: Han Ledger (Collective Resilience) ---
# ... (rest of the code above this line is unchanged) ...

def contribute_to_han(base_amount=10):
    """Calculates Han contribution with the Jeong Resonance Multiplier."""
    global GLOBAL_HAN_SCORE
    
    # 1. Get the current Jeong score (loyalty)
    jeong_data = calculate_jeong_connection()
    jeong_score = jeong_data['user_loyalty_score']
    
    # 2. Calculate the Resonance Multiplier (e.g., a score of 50 adds 50% bonus)
    multiplier = 1 + (jeong_score / 100.0)
    
    # 3. Calculate the precise contribution amount
    contribution_amount = round(base_amount * multiplier) # Round to nearest integer point
    
    with data_lock:
        GLOBAL_HAN_SCORE += contribution_amount
        
    return contribution_amount, GLOBAL_HAN_SCORE # Return both values

# ... (rest of the code below this line is unchanged) ...

@app.route('/han/contribute', methods=['POST'])
def handle_han_contribution():
    """Endpoint for a user to contribute to the Han Ledger (Tier 2 feature)."""
    # UNPACKING the two return values from the function
    contribution_amount, new_score = contribute_to_han(base_amount=10)
    
    return jsonify({
        "message": "Act of Resilience logged with Resonance Multiplier.", 
        "contribution_amount": contribution_amount,
        "new_han_score": new_score
    })
