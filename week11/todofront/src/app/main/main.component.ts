import { Component, OnInit } from '@angular/core';
import { TaskList, Task } from 'src/models/models';
import { isListLikeIterable } from '@angular/core/src/change_detection/change_detection_util';
import { ProviderService } from '../provider.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) { }

  public l: TaskList[] = [];
  public loading = true;

  public tasks: Task[] = [];

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.l = res;
      console.log(res);
    });
  } 
  taskListClicked = () => {
    console.log(this.l)
   }

  // getTasks(taskList: TaskList){
  //   this.provider.getTasks(taskList).then(res => {
  //     this.tasks = res;
  //   });
  // }

}
