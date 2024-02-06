import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditUsermanagementComponent } from './add-edit-usermanagement.component';

describe('AddEditUsermanagementComponent', () => {
  let component: AddEditUsermanagementComponent;
  let fixture: ComponentFixture<AddEditUsermanagementComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditUsermanagementComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditUsermanagementComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
