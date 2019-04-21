import { Component } from '@angular/core';
import { ProviderService } from './provider.service';
import { MainService } from 'src/services/main.service';
import {  TaskList} from 'src/models/models';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ProviderService, MainService]
})
export class AppComponent {
  public taskLists: TaskList[] = [];
  selectedTaskList = { id : -1, name: 'no'};
  sltl = '';
  constructor(private api: ProviderService) {
    this.getTaskLists();

  }
  getTaskLists = () =>{
      this.api.getAllTaskLists().subscribe(
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
    this.sltl = tl.name;
  }

  updateTaskList = () => {
    this.api.updateTasklist(this.selectedTaskList).subscribe(
      data => {
        this.getTaskLists();
      },
      error => {
        console.log(error);
      }
    );
  }
  createTaskList = () => {
    this.api.createTasklist(this.selectedTaskList).subscribe(
      data => {
        this.taskLists.push(data);
      },
      error => {
        console.log(error);
      }
    );
  }
  deleteTaskList = () => {
    this.api.deleteTasklist(this.selectedTaskList.id).subscribe(
      data => {
        this.getTaskLists();
      },
      error => {
        console.log(error);
      }
    );
  }
}

