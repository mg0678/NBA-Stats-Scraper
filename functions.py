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
    while answer not in ['1', '2', '3', '4']:
        answer = input('Pick a stat\n1. AST\n2. STL\n3. BLK\n4. PTS\n')
    
    if answer == '1':
        stat = 'AST'
    elif answer == '2':
        stat = 'STL'    
    elif answer == '3':
        stat = 'BLK'
    else:
        stat = 'PTS'
    return stat