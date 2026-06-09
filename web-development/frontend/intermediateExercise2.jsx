```html
<!DOCTYPE html>
<html>

<head>
    <title>Bootstrap Contact Form</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

</head>

<body class="bg-light">

    <div class="container py-5">

        <h2 class="text-center mb-4">Contact Us</h2>

        <form class="needs-validation" novalidate>

            <div class="mb-3">
                <label class="form-label">Name</label>
                <input type="text" class="form-control" required>
                <div class="invalid-feedback">
                    Please enter your name.
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label">Email</label>
                <input type="email" class="form-control" required>
                <div class="invalid-feedback">
                    Please enter a valid email.
                </div>
            </div>

            <div class="mb-3">
                <label class="form-label">Message</label>
                <textarea class="form-control" rows="4" required></textarea>
                <div class="invalid-feedback">
                    Please enter a message.
                </div>
            </div>

            <button class="btn btn-primary" type="submit">Send Message</button>

        </form>

    </div>

    <script>

        // Bootstrap validation script
        (() => {
            'use strict'

            const forms = document.querySelectorAll('.needs-validation')

            Array.from(forms).forEach(form => {
                form.addEventListener('submit', event => {
                    if (!form.checkValidity()) {
                        event.preventDefault()
                        event.stopPropagation()
                    }

                    form.classList.add('was-validated')
                }, false)
            })
        })()

    </script>

</body>

</html>
```