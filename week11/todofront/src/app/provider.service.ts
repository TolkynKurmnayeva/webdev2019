import { EventEmitter, Injectable } from '@angular/core';
import { MainService } from '../services/main.service';
import { TaskList , Task } from '../models/models';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<any> {
    return this.http.get('http://127.0.0.1:8000/task_list/', {}).toPromise().then(res => res);
  }
  // getTasks(taskList: TaskList): Promise<Task[]> {
  //   return this.get('http://localhost:8000/task_list/' + taskList.id + '/tasks', {});
  // }
}
