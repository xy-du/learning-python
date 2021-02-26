class BlackKnight:

    def __init__(self):
        self.members = ['an arm', 'another arm',
                        'a leg', 'another leg']
        self.phrases = ["'Tis but a scratch.",
                        "It's just a flesh wound.",
                        "I'm invincible!",
                        "All right, we'll call it a draw."]

    @property
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))


# del myobj.attribute
# is not something we do often, but it's supported
# methods:
#       @my_propety.deleter
#  or   member = property(member_getter, fdel=member_deleter)
if __name__ == '__main__':
    knight = BlackKnight()
    print(knight.member)
    del knight.member
    del knight.member
