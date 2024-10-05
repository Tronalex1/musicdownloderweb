from django.shortcuts import render
from ytmusicapi import YTMusic  # YouTube Music API
from django.http import FileResponse, HttpResponse
import subprocess

ytmusic = YTMusic('headers_auth.json')  # Initialize YouTube Music API

def search_music(request):
    if 'query' in request.GET:
        query = request.GET['query']
        search_results = ytmusic.search(query, filter="songs")
        return render(request, 'results.html', {'results': search_results})
    return render(request, 'index.html')

def download_music(request, song_id):
    format = request.GET.get('format', 'mp3')
    song_data = ytmusic.get_song(song_id)
    song_title = song_data['videoDetails']['title']

    # Here you would implement the logic to download the song using YouTube-dl or yt-dlp.
    # Example with yt-dlp:
    download_command = [
        "yt-dlp",
        f"https://www.youtube.com/watch?v={song_id}",
        "-x", "--audio-format", format, "-o", f"{song_title}.%(ext)s"
    ]
    
    subprocess.run(download_command, check=True)

    # Open the file and return it as a response
    file_path = f"{song_title}.{format}"
    file_pointer = open(file_path, 'rb')
    response = FileResponse(file_pointer, as_attachment=True, filename=f"{song_title}.{format}")
    
    return response
