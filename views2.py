<div class="container mt-4">
    <h1 class="text-center"><u>All Issued Books</u></h1>
    <table class="table table-hover" id="example">
        <thead>
            <tr class="text-center">
                <th>Sr.No</th>
                <th>Student</th>
                <th>Student ID</th>
                <th>Book Name</th>
                <th>ISBN</th>
                <th>Issued Date</th>
                <th>Expiry Date</th>
                <th>Fine</th>
                <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for i in details %}
            <tr class="text-center">
                <td>{{forloop.counter}}.</td>
                <td>{{i.0}}</td>
                <td>{{i.1}}</td>
                <td>{{i.2}}</td>
                <td>{{i.3}}</td>
                <td>{{i.4}}</td>
                <td>{{i.5}}</td>
                <td>₹ {{i.6}}</td>
                <td><a href="/delete_issue/{{book.id}}/" class="btn btn-danger" onclick="return confirm('Are you sure you want to delete this issued book details?')">Delete</a></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    </div>
