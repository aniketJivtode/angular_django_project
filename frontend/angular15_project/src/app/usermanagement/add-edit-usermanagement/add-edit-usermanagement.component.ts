import { Component, Input, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-usermanagement',
  templateUrl: './add-edit-usermanagement.component.html',
  styleUrls: ['./add-edit-usermanagement.component.css']
})
export class AddEditUsermanagementComponent implements OnInit {

  constructor(private service: SharedService) { }


  @Input() usermanag: any;
  id?: number;
  username !: string;
  email !: string;
  first_name !: string;
  last_name !: string;
  user_type !: number;
  department !: string;
  password !: string;
  // remaining column

  ngOnInit(): void {
    if (this.usermanag) {
      this.id = this.usermanag.id;
      this.username = this.usermanag.username;
      this.email = this.usermanag.email;
      this.first_name = this.usermanag.first_name;
      this.last_name = this.usermanag.last_name;
      this.department = this.usermanag.department;
      this.password = this.usermanag.password;
    }

  }

  addUserProfile() {
    var val = {
      id: this.id,
      username: this.username,
      email: this.email,
      first_name: this.first_name,
      last_name: this.last_name,
      department: this.department,
      password: this.password,
    };
    this.service.addUserProfile(val).subscribe(res => {
      alert(res.toString());
    });
  }

  updateUserProfile() {
    if (this.id) {
      var val = {
        id: this.id,
        username: this.username,
        email: this.email,
        first_name: this.first_name,
        last_name: this.last_name,
        department: this.department,
        password: this.password,
      };
      console.log('id values', val);

      // this.service.updateUserProfile(val).subscribe(res => {
      //   console.log('indise udpade userprofile', res);
      //   alert(res.toString());
      // });

      this.service.updateUserProfile(val).subscribe(res => {

        console.log('indise udpade userprofile', res);
        alert(res.toString());
      });
    }
    else {
      console.error('ID is not defined. Cannot update user profile.');
    }


  }
}
