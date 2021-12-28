import streamlit as st 
import pandas as pd 
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.espn.com/nba/injuries'

html = pd.read_html(url, header = 0)

nba_teams = ['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets', 'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers', 'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons', 'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers', 'LA Clippers', 'LA Lakers', 'Memphis Grizzlies', 'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves', 'New Orleans Pelicans', 'New York Knicks', 'OKC Thunder', 'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns', 'Portland Trail Blazers', 'Sacramento Kings', 'San Antonio Spurs', 'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']

st.title('NBA Injury Report')

st.sidebar.header('Select A Team')

selected_team = st.sidebar.selectbox('Team', nba_teams)


if selected_team == 'Atlanta Hawks':
    df = html[0]
    st.write(df)

if selected_team == 'Boston Celtics':
    df = html[1]
    st.write(df)

if selected_team == 'Brooklyn Nets':
    df = html[2]
    st.write(df)

if selected_team == 'Charlotte Hornets':
    df = html[3]
    st.write(df)

if selected_team == 'Chicago Bulls':
    df = html[4]
    st.write(df)

if selected_team == 'Cleveland Cavaliers':
    df = html[5]
    st.write(df)

if selected_team == 'Dallas Mavericks':
    df = html[6]
    st.write(df)

if selected_team == 'Denver Nuggets':
    df = html[7]
    st.write(df)

if selected_team == 'Detroit Pistons':
    df = html[8]
    st.write(df)

if selected_team == 'Golden State Warriors':
    df = html[9]
    st.write(df)

if selected_team == 'Houston Rockets':
    df = html[10]
    st.write(df)

if selected_team == 'Indiana Pacers':
    df = html[11]
    st.write(df)

if selected_team == 'LA Clippers':
    df = html[12]
    st.write(df)

if selected_team == 'LA Lakers':
    df = html[13]
    st.write(df)

if selected_team == 'Memphis Grizzlies':
    df = html[14]
    st.write(df)

if selected_team == 'Miami Heat':
    df = html[15]
    st.write(df)

if selected_team == 'Milwaukee Bucks':
    df = html[16]
    st.write(df)

if selected_team == 'Minnesota Timberwolves':
    df = html[17]
    st.write(df)

if selected_team == 'New Orleans Pelicans':
    df = html[18]
    st.write(df)

if selected_team == 'New York Knicks':
    df = html[19]
    st.write(df)

if selected_team == 'OKC Thunder':
    df = html[20]
    st.write(df)

if selected_team == 'Orlando Magic':
    df = html[21]
    st.write(df)

if selected_team == 'Philadelphia 76ers':
    df = html[22]
    st.write(df)

if selected_team == 'Phoenix Suns':
    df = html[23]
    st.write(df)

if selected_team == 'Portland Trail Blazers':
    df = html[24]
    st.write(df)

if selected_team == 'Sacramento Kings':
    df = html[25]
    st.write(df)

if selected_team == 'San Antonio Spurs':
    df = html[26]
    st.write(df)

if selected_team == 'Toronto Raptors':
    df = html[27]
    st.write(df)

if selected_team == 'Utah Jazz':
    df = html[28]
    st.write(df)

if selected_team == 'Washington Wizards':
    df = html[29]
    st.write(df)