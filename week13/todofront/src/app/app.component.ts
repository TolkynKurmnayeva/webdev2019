import { Component, OnInit } from '@angular/core';
import { ProviderService } from './provider.service';
import { MainService } from 'src/services/main.service';
import {  TaskList} from 'src/models/models';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ProviderService, MainService]
})
export class AppComponent implements OnInit {
  public taskLists: TaskList[] = [];

  public selectedTaskList = { id : -1, name: 'no'};
  
  public isLogged = false;

  public login = '';
  public password = '';




  constructor(private provider: ProviderService) {

    

  }
  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if ( this.isLogged) {
      this.getTaskLists();
    }

  }
  getTaskLists = () =>{
      this.provider.getAllTaskLists().subscribe(
        data => {
          this.taskLists = data;
        },
        error => {
          console.log(error);
        }
      )
  }

  tlClicked = (tl) => {
    this.selectedTaskList = {id:tl.id, name: tl.name};
    
  }

  updateTaskList = () => {
    this.provider.updateTasklist(this.selectedTaskList).subscribe(
      data => {
        this.getTaskLists();
      },
      error => {
        console.log(error);
      }
    );
  }

  createTaskList = () => {
    this.provider.createTasklist(this.selectedTaskList).subscribe(
      data => {
        this.taskLists.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }
  deleteTaskList = () => {
    this.provider.deleteTasklist(this.selectedTaskList.id).subscribe(
      data => {
        this.getTaskLists();
      },
      error => {
        console.log(error);
      }
    );
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTaskLists();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }
}

