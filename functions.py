def perGameOrTotal():
    stat_pg_tot = 0
    while stat_pg_tot not in ['1','2']:
        stat_pg_tot = input('Get Stats\n1. Per Game\n2. Season Totals\n')
    if stat_pg_tot == '1':
        url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
    else:
        url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
    return url

def pickStat(answer):
    stat ='z'
    while answer not in ['1', '2', '3', '4','5']:
        answer = input('Pick a stat\n1. AST\n2. REB\n3. STL\n4. BLK\n5. PTS\n')
    
    if answer == '1':
        stat = 'AST'
    elif answer == '2':
        stat = 'REB'
    elif answer == '3':
        stat = 'STL'    
    elif answer == '4':
        stat = 'BLK'
    else:
        stat = 'PTS'
    return stat

def teamSelection():
    team = 'z'
    answer = 0
    teams = []
    for i in range(30):
        teams.append(str(i+1))

    print('1.  Atlanta       2.  Boston        3.  Brooklyn')
    print('4.  Charlotte     5.  Chicago       6.  Cleveland')
    print('7.  Dallas        8.  Denver        9.  Detroit')
    print('10. Golden State  11. Houston       12. Indiana')
    print('13. LA Clippers   14. LA Lakers     15. Memphis')
    print('16. Miami         17. Milwaukee     18. Minnesota')
    print('19. New Orleans   20. New York      21. Oklahoma City')
    print('22. Orlando       23. Philadelphia  24. Phoenix')
    print('25. Portland      26. Sacramento    27. San Antonio')
    print('28. Toronto       29. Utah          30. Washington')
    
    while answer not in teams:
        answer = input('Pick Team:\n')
    if answer == '1':
        team = 'ATL'
    elif answer == '2':
        team = 'BOS'
    elif answer == '3':
        team = 'BRK'
    elif answer == '4':
        team = 'CHO'
    elif answer == '5':
        team = 'CHI'
    elif answer == '6':
        team = 'CLE'    
    elif answer == '7':
        team = 'DAL'
    elif answer == '8':
        team = 'DEN'
    elif answer == '9':
        team = 'DET'
    elif answer == '10':
        team = 'GDW'
    elif answer == '11':
        team = 'HOU'
    elif answer == '12':
        team = 'IND'
    elif answer == '13':
        team = 'LAC'
    elif answer == '14':
        team = 'LAL'
    elif answer == '15':
        team = 'MEM'
    elif answer == '16':
        team = 'MIA'
    elif answer == '17':
        team = 'MIL'
    elif answer == '18':
        team = 'MIN'
    elif answer == '19':
        team = 'NOP'
    elif answer == '20':
        team = 'NYK'
    elif answer == '21':
        team = 'OKC'
    elif answer == '22':
        team = 'ORL'
    elif answer == '23':
        team = 'PHI'
    elif answer == '24':
        team = 'PHO'
    elif answer == '25':
        team = 'POR'
    elif answer == '26':
        team = 'SAC'
    elif answer == '27':
        team = 'SAS'
    elif answer == '28':
        team = 'TOR'
    elif answer == '29':
        team = 'UTA'
    else:
        team = 'WAS'

    return team
