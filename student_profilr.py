<div class="container profile">
        <div class="row">
            <div class="col-md-4">
                <div class="profile-img">
                    <img src="{{user.student.image.url}}" alt="" width="310px" height="270px">
                </div>
            </div>
            <div class="col-md-8">
                <div class="profile-tab">
                    <div class="tab-pane">
                        <div class="row">
                            <div class="col-md-6">
                                <label>ID:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.id}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Username:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Full Name:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.get_full_name}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Email:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.email}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Phone Number:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.student.phone}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Branch:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.student.branch}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Class:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.student.classroom}}</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-md-6">
                                <label>Roll Number:</label>
                            </div>
                            <div class="col-md-6">
                                <p>{{user.student.roll_no}}</p>
                            </div>
                        </div>
                    </div>
                    <a href="/edit_profile/" style="width: 9rem;" class="btn btn-outline-primary mt-3">Edit Profile</a>
                </div>
            </div>
</div>
</div>
