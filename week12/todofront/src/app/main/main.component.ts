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

  public taskLists: TaskList[] = [];
  public loading = false;

  public tasks: Task[] = [];

  ngOnInit() {
    // this.provider.getTaskLists().then(res => {
    //   this.taskLists = res;
    //   console.log(res);
    // });
  }

  // getTasks(taskList: TaskList){
  //   this.provider.getTasks(taskList).then(res1 => {
  //     this.tasks = res1;
  //   });
  // }

}
