from pytube import YouTube

def choice():
    while True :
        global video_link
        video_link = input('Enter the link of the video you want to Download :- ')
        global search_query, title, thumbnail
        search_query = YouTube(f'{video_link}')

        title = search_query.title
        thumbnail = search_query.thumbnail_url
        audio()

def audio():
    streams = search_query.streams.filter(only_audio=True)

    print(f'{streams}')
    print('\n')
    print(f'Views : {video_link}.views')
    print('\n')
    print(f'Ratings : {video_link}.rating')
    print('\n')
    print(f'Description : {video_link}.description')
    print('\n')
    print(f'Length : {video_link}.length')    
    print('\n')

    tag = input('Enter the desired tag for streams list :- ')

    print('\n')
    print(f'{title}')
    print('\n')
    print(f'{thumbnail}')
    print('\n')
    print('Downloading.........')

    stream_quality_download = search_query.streams.get_by_itag(f'{tag}').download()

    print('\n')
    print('Downloaded Succesfully')
    print('\n')


choice()

# quality = search_query.streams.filter(only_video=True)


