import constants
import copy

if __name__ == "__main__":

    clean_PLAYERS = []
    clean_TEAMS = []

    for players in constants.PLAYERS:
        clean_PLAYERS.append(players)

    for teams in constants.TEAMS:
        clean_TEAMS.append(teams)

    def clean_data(cleaned_PLAYERS):
        for iterate in range(len(cleaned_PLAYERS)):
            height = [
                int(ht_index) for ht_index
                in cleaned_PLAYERS[iterate]['height'].split(' ')
                if ht_index.isdigit()
            ]
            cleaned_PLAYERS[iterate]['height'] = (height[0])

            if cleaned_PLAYERS[iterate]['experience'].lower() == 'yes':
                cleaned_PLAYERS[iterate]['experience'] = True

            elif cleaned_PLAYERS[iterate]['experience'].lower() == 'no':
                cleaned_PLAYERS[iterate]['experience'] = False

        return cleaned_PLAYERS

    def balance_TEAMS(balanced_PLAYERS, balanced_TEAMS):
        experience_count = 0
        inexperience_count = 0

        for player in balanced_PLAYERS:
            if player['experience']:
                experience_count += 1
            else:
                inexperience_count += 1
        print(experience_count)
        print(inexperience_count)

        spread_experience = int(experience_count / (len(constants.TEAMS)))
        spread_inexperience = int(inexperience_count / (len(constants.TEAMS)))

        for team in balanced_TEAMS:
            count_experience = 0
            count_inexperience = 0

            for playerr in balanced_PLAYERS:
                if ('team' not in playerr and
                        count_experience < spread_experience and
                        playerr.get('experience') is True):
                    playerr.update({'team': team})
                    count_experience += 1
                elif ('team' not in playerr and count_inexperience <
                        spread_inexperience and
                        playerr.get('experience') is False):
                        playerr.update({'team': team})
                        count_inexperience += 1

        return balanced_PLAYERS

    def number_players_team(total_players, team):
        kount = 0

        for playz in total_players:
            if team == playz.get('team'):
                kount += 1

        return kount

    def stats_menu():
        while True:

            while True:

                try:
                    menu_choice = int(
                        input(
                            "\n\nBASKETBALL TEAM STATS TOOL \n\n----MENU----\n\n"
                            "Would you like to review team stats? \n1) yes\n"
                            "2) no\n\nEnter Choice: \n"
                        ))

                    if menu_choice == 1:
                        team_menu(clean_TEAMS)
                        break

                    elif menu_choice == 2:
                        exit()

                except ValueError as err:
                    print("\nYour entry was incorrect, please try again\n")

    def team_menu(clean_TEAMZ):
        print("\nTeams:\n")
        [print(f"{number}) {teamz}")
         for number, teamz in enumerate(clean_TEAMZ, 1)]

        while True:

            try:
                option = int(
                    input(
                            "\nPlease choose a team to "
                            "review their stats: "
                            )) - 1
                if option in range(0, len(clean_TEAMZ)+1):
                    break
            except ValueError as err:
                print("\nYour entry was incorrect, please try again\n")

        print(option)
        team_stats(clean_TEAMS, clean_PLAYERS, option)

    def team_stats(cleaner_TEAMS, cleaner_PLAYERS, option):
        number_players = 0
        total_experienced = 0
        total_inexperienced = 0
        average_height = 0
        playerz_on_team = []
        guardians_of_teams = []
        current_team = cleaner_TEAMS[option]

        for playerz in cleaner_PLAYERS:
            if playerz.get('team') == cleaner_TEAMS[option]:
                number_players += 1
                playerz_on_team.append(playerz['name'])
                guardians_of_teams.append(
                    playerz['guardians'].replace(' and ', ', '))

                if playerz.get('experience') is True:
                    total_experienced += 1
                elif playerz.get('experience') is False:
                    total_inexperienced += 1
                average_height = average_height + playerz.get('height')

        playerz_on_team = ", ".join(playerz_on_team)
        guardians_of_teams = ", ".join(guardians_of_teams)

        average_height = round((average_height/number_players), 2)

        print(
            f"Team: {current_team}"
            "\n--------------------\n"
            f"\nTotal players: {number_players}\n"
            f"Total experienced: {total_experienced}\n"
            f"Total inexperienced: {total_inexperienced}\n"
            f"Average height: {average_height}\n"
            "\n\n"
            "\nPlayers on Team: \n"
            f"    {playerz_on_team}\n"
            "Player's guardians: \n"
            f"	{guardians_of_teams}"

        )

    clean_data(clean_PLAYERS)
    balance_TEAMS(clean_PLAYERS, clean_TEAMS)
    stats_menu()

