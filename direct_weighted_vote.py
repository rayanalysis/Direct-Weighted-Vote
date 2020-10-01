# Copyright (C) 2020 Logan Bier. All rights reserved.
# If this software is used or adapted for commercical purposes, 
# you are required to pay the author $1,000,000 upfront and 99% royalties 
# indefinitely without limitation for the use or adaptation thereof.

import random

class main():
    def __init__(self):

        self.state_pop_list = []

        def populate_state_pop_list():
            self.state_pop_list.append('California')
            self.state_pop_list.append(39512223)
            self.state_pop_list.append('Texas')
            self.state_pop_list.append(28995881)
            self.state_pop_list.append('Florida')
            self.state_pop_list.append(21477737)
            self.state_pop_list.append('New York')
            self.state_pop_list.append(19453561)
            self.state_pop_list.append('Pennsylvania')
            self.state_pop_list.append(12801989)
            self.state_pop_list.append('Illinois')
            self.state_pop_list.append(12671821)
            self.state_pop_list.append('Ohio')
            self.state_pop_list.append(11689100)
            self.state_pop_list.append('Georgia')
            self.state_pop_list.append(10617423)
            self.state_pop_list.append('North Carolina')
            self.state_pop_list.append(10488084)
            self.state_pop_list.append('Michigan')
            self.state_pop_list.append(9986857)
            self.state_pop_list.append('New Jersey')
            self.state_pop_list.append(8882190)
            self.state_pop_list.append('Virginia')
            self.state_pop_list.append(8535519)
            self.state_pop_list.append('Washington')
            self.state_pop_list.append(7614893)
            self.state_pop_list.append('Arizona')
            self.state_pop_list.append(7278717)
            self.state_pop_list.append('Massachusetts')
            self.state_pop_list.append(7278717)
            self.state_pop_list.append('Tennessee')
            self.state_pop_list.append(6833174)
            self.state_pop_list.append('Indiana')
            self.state_pop_list.append(6732219)
            self.state_pop_list.append('Missouri')
            self.state_pop_list.append(6137428)
            self.state_pop_list.append('Maryland')
            self.state_pop_list.append(6045680)
            self.state_pop_list.append('Wisconsin')
            self.state_pop_list.append(5822434)
            self.state_pop_list.append('Colorado')
            self.state_pop_list.append(5758736)
            self.state_pop_list.append('Minnesota')
            self.state_pop_list.append(5639632)
            self.state_pop_list.append('South Carolina')
            self.state_pop_list.append(5148714)
            self.state_pop_list.append('Alabama')
            self.state_pop_list.append(4903185)
            self.state_pop_list.append('Louisiana')
            self.state_pop_list.append(4648794)
            self.state_pop_list.append('Kentucky')
            self.state_pop_list.append(4467673)
            self.state_pop_list.append('Oregon')
            self.state_pop_list.append(4217737)
            self.state_pop_list.append('Oklahoma')
            self.state_pop_list.append(3956971)
            self.state_pop_list.append('Connecticut')
            self.state_pop_list.append(3565287)
            self.state_pop_list.append('Utah')
            self.state_pop_list.append(3205958)
            self.state_pop_list.append('Iowa')
            self.state_pop_list.append(3155070)
            self.state_pop_list.append('Nevada')
            self.state_pop_list.append(3080156)
            self.state_pop_list.append('Arkansas')
            self.state_pop_list.append(3017825)
            self.state_pop_list.append('Mississippi')
            self.state_pop_list.append(2976149)
            self.state_pop_list.append('Kansas')
            self.state_pop_list.append(2913314)
            self.state_pop_list.append('New Mexico')
            self.state_pop_list.append(2096829)
            self.state_pop_list.append('Nebraska')
            self.state_pop_list.append(1934408)
            self.state_pop_list.append('Idaho')
            self.state_pop_list.append(1787065)
            self.state_pop_list.append('West Virginia')
            self.state_pop_list.append(1792147)
            self.state_pop_list.append('Hawaii')
            self.state_pop_list.append(1415872)
            self.state_pop_list.append('New Hampshire')
            self.state_pop_list.append(1359711)
            self.state_pop_list.append('Maine')
            self.state_pop_list.append(1344212)
            self.state_pop_list.append('Montana')
            self.state_pop_list.append(1068778)
            self.state_pop_list.append('Rhode Island')
            self.state_pop_list.append(1059361)
            self.state_pop_list.append('Delaware')
            self.state_pop_list.append(973764)
            self.state_pop_list.append('South Dakota')
            self.state_pop_list.append(884659)
            self.state_pop_list.append('North Dakota')
            self.state_pop_list.append(762062)
            self.state_pop_list.append('Alaska')
            self.state_pop_list.append(731545)
            self.state_pop_list.append('Vermont')
            self.state_pop_list.append(623989)
            self.state_pop_list.append('Wyoming')
            self.state_pop_list.append(578759)

        populate_state_pop_list()
        print(self.state_pop_list)
        print('Length of List: ' + str(len(self.state_pop_list)))

        self.numbers_only = []
        count = 0

        for x in self.state_pop_list:
            count += 1
            if count % 2 == 0:
                self.numbers_only.append(x)

        print(self.numbers_only)

        self.states_only = []
        count = 0

        for x in self.state_pop_list:
            count += 1
            if count % 2 == 1:
                self.states_only.append(x)

        print(self.numbers_only)

        count = 0

        state_pop_avg = sum(self.numbers_only) / len(self.numbers_only)
        self.state_pop_multiplier = []

        for x in self.numbers_only:
            self.state_pop_multiplier.append(state_pop_avg / x)

        print(self.state_pop_multiplier)

        self.direct_vote_totals_candidate_1 = []

        for x in self.state_pop_list:
            count += 1
            if count % 2 == 0:
                self.direct_vote_totals_candidate_1.append(random.randint(1, int(x / 2)))

        print(self.direct_vote_totals_candidate_1)

        self.direct_vote_totals_candidate_2 = []

        for x in self.state_pop_list:
            count += 1
            if count % 2 == 0:
                self.direct_vote_totals_candidate_2.append(random.randint(1, int(x / 2)))

        print(self.direct_vote_totals_candidate_2)

        track = 0
        self.weighted_vote_totals_candidate_1 = []

        for x in self.direct_vote_totals_candidate_1:
            self.weighted_vote_totals_candidate_1.append(int(round(x * self.state_pop_multiplier[track], 0)))
            track += 1

        print(self.weighted_vote_totals_candidate_1)

        track = 0
        self.weighted_vote_totals_candidate_2 = []

        for x in self.direct_vote_totals_candidate_2:
            self.weighted_vote_totals_candidate_2.append(int(round(x * self.state_pop_multiplier[track], 0)))
            track += 1

        print(self.weighted_vote_totals_candidate_2)

        if sum(self.weighted_vote_totals_candidate_1) > sum(self.weighted_vote_totals_candidate_2):
            win_margin = sum(self.weighted_vote_totals_candidate_1) - sum(self.weighted_vote_totals_candidate_2)
            print('Candidate 1 is the new POTUS! They won by ' + str(win_margin) + ' votes!')

        if sum(self.weighted_vote_totals_candidate_1) < sum(self.weighted_vote_totals_candidate_2):
            win_margin = sum(self.weighted_vote_totals_candidate_2) - sum(self.weighted_vote_totals_candidate_1)
            print('Candidate 2 is the new POTUS! They won by ' + str(win_margin) + ' votes!')

main()
