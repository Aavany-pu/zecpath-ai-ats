def get_processing_strategy():
    processing_strategy = {
        "Resume Processing": {
            "Processing Type": "Async",
            "Reason": "Resume processing can run as a background task."
        },
        "Real-Time Interview Scoring": {
            "Processing Type": "Sync",
            "Reason": "Interview scoring requires an immediate response."
        }
    }

    return {
        "Status": "Processing Strategy Defined",
        "Processing Strategy": processing_strategy
    }