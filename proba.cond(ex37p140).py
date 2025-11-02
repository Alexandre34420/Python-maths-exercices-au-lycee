def proba_cond(card):
    A_et_B, A_et_nonB, nonA_et_B, nonA_et_nonB = card
    A = A_et_B + A_et_nonB #Card(A) = Card(A ∩ B) + Card(A ∩ nonB)
    B = A_et_B + nonA_et_B #Card(B) = Card(A ∩ B) + Card(nonA ∩ B)
    p_B_sachant_A = A_et_B/A #p(B_sachant_A) = Card(A ∩ B)/Card(A)
    p_A_sachant_B = A_et_B/B #p(A_sachant_B) = Card(A ∩ B)/Card(B)
    return [p_B_sachant_A, p_A_sachant_B]