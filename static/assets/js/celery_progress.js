document.addEventListener("DOMContentLoaded", function () {
  var progressUrl = "{% url 'celery_progress:task_status' task_id %}";
  CeleryProgressBar.initProgressBar(progressUrl);
});
