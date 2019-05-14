import { Component } from '@angular/core';
import { ProviderService } from './provider.service';
import { MainService } from 'src/services/main.service';
import {  TaskList} from 'src/models/models'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ProviderService, MainService]
})
export class AppComponent {
  public taskLists: TaskList[] = [];
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
}
