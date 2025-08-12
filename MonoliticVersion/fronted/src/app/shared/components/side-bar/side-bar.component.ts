import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { PlaylistService, Playlist } from 'src/app/core/services/playlist.service';

@Component({
  selector: 'app-side-bar',
  standalone: true,
  imports: [CommonModule, RouterModule, FormsModule],
  templateUrl: './side-bar.component.html',
  styleUrl: './side-bar.component.css'
})
export class SideBarComponent implements OnInit {

  mainMenu: {
    defaultOptions: Array<any>, accessLink: Array<any>
  } = { defaultOptions: [], accessLink: [] }

  customOptions: Array<any> = [];
  showCreateModal: boolean = false;
  newPlaylistName: string = '';

  constructor(public router: Router, private playlistService: PlaylistService) { }

  ngOnInit(): void {
    this.mainMenu.defaultOptions = [
      {
        name: 'Home',
        icon: 'uil uil-estate',
        router: ['/home']
      },
      {
        name: 'Buscar',
        icon: 'uil uil-search',
        router: ['/home/history']
      },{
        name: 'Tu biblioteca',
        icon: 'uil uil-chart',
        router: ['/home/favorites'],
      }
    ];

    this.mainMenu.accessLink = [
      {
        name: 'Crear lista',
        icon: 'uil-plus-square',
        action: () => this.openCreateModal()
      },
      {
        name: 'Canciones que te gustan',
        icon: 'uil-heart-medical',
        router: ['/home/favorites/liked-songs']
      },
      {
        name: 'Subir música',
        icon: 'uil-cloud-upload',
        router: ['/home/tracks/admin']
      }
    ];

    this.customOptions = [];
  }

  openCreateModal(): void {
    this.showCreateModal = true;
    this.newPlaylistName = '';
  }

  closeCreateModal(): void {
    this.showCreateModal = false;
    this.newPlaylistName = '';
  }

  createPlaylist(): void {
    if (!this.newPlaylistName.trim()) return;
    this.playlistService.createPlaylist(this.newPlaylistName.trim()).subscribe({
      next: (playlist: Playlist) => {
        this.customOptions.push({ name: playlist.name, router: ['/'] });
        this.closeCreateModal();
      },
      error: () => {
        alert('Error al crear la lista');
      }
    });
  }
}
