import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service';

@Component({
  selector: 'app-show-usermanagement',
  templateUrl: './show-usermanagement.component.html',
  styleUrls: ['./show-usermanagement.component.css']
})
export class ShowUsermanagementComponent implements OnInit {
 
  constructor(private service:SharedService){ }

  UsermanagementList :any=[];
 
  
  ModalTitle !:String;
  ActivateAddEditUserComp : boolean = false;
  usermanag : any;

  ngOnInit(): void{
    this.refreshUserList();
  }


  refreshUserList(){
    this.service.getProfileList().subscribe(data =>{
      this.UsermanagementList=data;
      console.log(data)
    });
  }

  addClick(){
    this.usermanag={
      id:0,
      username:'',
      email:'',
      first_name: '',
      last_name: '',
      department:'',
      password:'',
    }
    this.ModalTitle = "Add UserProfile";
    this.ActivateAddEditUserComp = true;
  }

  editClick(item: any){
    this.usermanag = item;
    this.ModalTitle = "Edit User Profile";
    this.ActivateAddEditUserComp = true;

  }

  
  // deleteClick(item: { id: any; }){
  //   if(confirm('Are you sure??')){
  //     this.service.deleteProfile(item.id).subscribe(data=>{
  //       alert(data.toString());
  //       this.refreshUserList();
  //     })
  //   }
  // }

  deleteClick(item: any){
    if (confirm('Are you sure??')) {
      this.service.deleteProfile(item.id).subscribe(data => {
        if (data !== null && data !== undefined) {
          alert(data.toString());
          this.refreshUserList();
        } else {
          // Handle the case where data is null or undefined
          console.log('this is a data value',data);
          // console.error('Delete operation returned null or undefined data');
          // Optionally, you can display a user-friendly error message
          // alert('Error deleting the profile. Please try again.');
        }
      });
    }
  }
  

  closeClick(){
    this.ActivateAddEditUserComp = false;
    this.refreshUserList();
  }


}

