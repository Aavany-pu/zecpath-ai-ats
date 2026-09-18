class ConversationState:

    def __init__(self):

        self.current_question = 0

        self.retry_count = 0

        self.status = "ACTIVE"

    def next_question(self):

        self.current_question += 1

        self.retry_count = 0

    def retry(self):

        self.retry_count += 1

    def end(self):

        self.status = "ENDED"