# SPLITTERS

def GENERATE_INFO(eth_value):
    profit_percentage = 0.49
    pioneer_reward_pool_percentage = 0.06
    community_multisig_percentage = 0.32
    developers_multisig_percentage = 0.13
    x7r_percentage = 0.10
    x7dao_percentage = 0.10
    x7_constellations_percentage = 0.10
    lending_pool_percentage = 0.20
    treasury_percentage = 0.50
    treasury_share = eth_value * treasury_percentage

    profit_share = treasury_share * profit_percentage
    pioneer_reward_pool_share = treasury_share * pioneer_reward_pool_percentage
    community_multisig_share = treasury_share * community_multisig_percentage
    developers_multisig_share = treasury_share * developers_multisig_percentage
    x7r_share = eth_value * x7r_percentage
    x7dao_share = eth_value * x7dao_percentage
    x7_constellations_share = eth_value * x7_constellations_percentage
    lending_pool_share = eth_value * lending_pool_percentage

    return {
        "X7R": x7r_share,
        "X7DAO": x7dao_share,
        "X7 Constellations": x7_constellations_share,
        "Lending Pool": lending_pool_share,
        "Treasury": treasury_share,
        "Profit Sharing Total": profit_share,
        "Pioneer Reward Pool": pioneer_reward_pool_share,
        "Community Multi Sig": community_multisig_share,
        "Developers Multi Sig": developers_multisig_share,
    }
