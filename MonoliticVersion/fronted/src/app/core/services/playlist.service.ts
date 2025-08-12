import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Playlist {
  id?: number;
  name: string;
  tracks?: any[];
}

@Injectable({
  providedIn: 'root'
})
export class PlaylistService {
  private apiUrl = 'http://localhost:5000/api/playlists';

  constructor(private http: HttpClient) {}

  createPlaylist(name: string): Observable<Playlist> {
    return this.http.post<Playlist>(`${this.apiUrl}/create`, { name });
  }

  getUserPlaylists(userId: number): Observable<Playlist[]> {
    return this.http.get<Playlist[]>(`${this.apiUrl}/user/${userId}`);
  }

  addTrackToPlaylist(playlistId: number, trackId: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/${playlistId}/add-track`, { trackId });
  }
}
