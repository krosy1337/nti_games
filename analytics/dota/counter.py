class Counter():
    def __init__(self):
        self.role = 0
        self.pk_weight = 0
        self.num = 0
        self.comparing = 0
        self.fantasy = 0

    def count_role(self):
        return self.role * 100 / self.num if self.num != 0 else 0

    def count_pk(self):
        return self.pk_weight * 100 / self.num if self.num != 0 else 0

    def count_quality(self):
        if self.num != 0:
            return [self.comparing * 100 / (self.num * 9), self.fantasy * 100 / (20 * self.num)]
        return [0, 0]

    def check_is_empty(self):
        return True if self.num == 0 else False
