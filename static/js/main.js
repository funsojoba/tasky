window.addEventListener('DOMContentLoaded', function() {
    const openButton = document.getElementById('hambugger');
    const closeButton = document.getElementById('closeBar');
    const sidebar = document.getElementById('cta-button-sidebar');

    openButton.addEventListener('click', function() {
        // Toggle the sidebar
        if (sidebar.classList.contains('-translate-x-full')) {
            sidebar.classList.remove('-translate-x-full');
        } else {
            sidebar.classList.add('-translate-x-full');
        }
    });
    closeButton.addEventListener('click', function(){
        sidebar.classList.add('-translate-x-full');
    })



  let baseUrl = window.location.host;

  if (baseUrl.startsWith("localhost:8000")) {
      baseUrl = "http://" + baseUrl;
  }

  // SEARCH ENDPOINT
  const url = baseUrl + '/tasks/api/tasks';
  let searchInput = document.querySelector('input[type="search"]');
  let taskSort = document.getElementById('task-sort');
  let hambuggerButton = document.getElementById("hambugger")
  let sideBar = document.getElementById("cta-button-sidebar")
  
  const formatDate = (timestamp) => {
    const date = new Date(timestamp);
  
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
    });
  };

  searchInput.addEventListener('input', function() {
      let query = searchInput.value;

      // Perform an AJAX request
      $.ajax({
          url: `/tasks/api/tasks`,  // API endpoint URL
          data: {
              'search': query
          },
          success: function(data) {
              console.log("DATA: ", data);

              // Update task sections based on status
              const taskSection = document.getElementById("tasks")

              taskSection.innerHTML = '';

              data.forEach(task => {
                  const taskHtml = `
                      <div class="task-container">
                          <div class="flex mb-1 justify-between items-center">
                              <small class="p-3 py-2 rounded ${task.priority == 'High' ? 'bg-[#FFD1D1] text-[#9F3131]' : task.priority == 'Medium' ? 'bg-[#FED2A5] text-[#89531B]' : 'bg-[#E3FFE2] text-[#268324]'}">${task.priority}</small>
                              <small class="p-3 py-2 rounded bg-white shadow-md">${formatDate(task.due_date)}</small>
                              <small class="px-3 py-2 bg-[#ECE5FF] text-[#5824F0] rounded">${task.category}</small>
                          </div>
                          <div class="bg-[#E8E8E8] mb-7 rounded p-3 w-[300px] mb-[10px]">
                              <h3>${task.title}</h3>
                              <p>${task.description.length > 100 ? task.description.substring(0, 100) + '...' : task.description}</p>
                              <div class="flex gap-[10px] justify-between items-center">
                                  <div class="flex items-center gap-[5px]">
                                      ${task.assigned_to.map(user => `<span class="flex items-center justify-center w-[30px] h-[30px] bg-[#3939E6] text-[#fff] rounded-full border border-solid border-white mx-[-5px]">${user.username.slice(0, 1)}</span>`).join('')}
                                  </div>
                                  <div>
                                      <a href="/tasks/detail/${task.id}" class="text-[#3838E6]"><i class="fa-regular fa-eye"></i></a>
                                      <button class="text-[#3838E6]"><i class="fa-solid fa-trash-can"></i></button>
                                      <button class="text-[#3838E6]"><i class="fa-solid fa-pen"></i></button>
                                  </div>
                              </div>
                          </div>
                      </div>
                  `;
                  taskSection.innerHTML += taskHtml;

              });
          }
      });
  });

  taskSort.addEventListener('change', function(){
    let query = taskSort.value;

    $.ajax({
        url: `/tasks/api/tasks`,  // API endpoint URL
        data: {
            'sort': query
        },
        success: function(data) {
            console.log("DATA: ", data);

            // Update task sections based on status
            const taskSection = document.getElementById("tasks")

            taskSection.innerHTML = '';

            data.forEach(task => {
                const taskHtml = `
                    <div class="task-container">
                        <div class="flex mb-1 justify-between items-center">
                            <small class="p-3 py-2 rounded ${task.priority == 'High' ? 'bg-[#FFD1D1] text-[#9F3131]' : task.priority == 'Medium' ? 'bg-[#FED2A5] text-[#89531B]' : 'bg-[#E3FFE2] text-[#268324]'}">${task.priority}</small>
                            <small class="p-3 py-2 rounded bg-white shadow-md">${formatDate(task.due_date)}</small>
                            <small class="px-3 py-2 bg-[#ECE5FF] text-[#5824F0] rounded">${task.category}</small>
                        </div>
                        <div class="bg-[#E8E8E8] mb-7 rounded p-3 w-[300px] mb-[10px]">
                            <h3>${task.title}</h3>
                            <p>${task.description.length > 100 ? task.description.substring(0, 100) + '...' : task.description}</p>
                            <div class="flex gap-[10px] justify-between items-center">
                                <div class="flex items-center gap-[5px]">
                                    ${task.assigned_to.map(user => `<span class="flex items-center justify-center w-[30px] h-[30px] bg-[#3939E6] text-[#fff] rounded-full border border-solid border-white mx-[-5px]">${user.username.slice(0, 1)}</span>`).join('')}
                                </div>
                                <div>
                                    <a href="/tasks/detail/${task.id}" class="text-[#3838E6]"><i class="fa-regular fa-eye"></i></a>
                                    <button class="text-[#3838E6]"><i class="fa-solid fa-trash-can"></i></button>
                                    <button class="text-[#3838E6]"><i class="fa-solid fa-pen"></i></button>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                taskSection.innerHTML += taskHtml;

            });
        }
    });

  })

});
