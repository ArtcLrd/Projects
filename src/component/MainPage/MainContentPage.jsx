import React, {useState, useRef, useEffect} from "react";
import { Container, Row, Col, Button, Form, ToggleButton, ListGroup, Dropdown, Accordion, Badge,Card,Modal } from "react-bootstrap";

import { CiBellOn, CiRepeat, CiCalendarDate } from "react-icons/ci";
import { FaStar, FaRegStar, FaTrash, FaFilter, FaCheckCircle } from "react-icons/fa";
import { IoMdClose } from "react-icons/io";
import { useDispatch, useSelector } from 'react-redux';
import { 
  addTask, 
  removeTask, 
  toggleTask, 
  setFilter, 
  clearCompleted,
  toggleFavorite
} from '../Slices/TaskSlice';


function AddTask(){
    const dispatch = useDispatch();
    const [newTask, setNewTask] = useState('');
    const { items: tasks } = useSelector(state => state.tasks);
    const [text, setText] = useState("");
    const textareaRef = useRef(null);
    const [isFavorite, setIsFavorite] = useState(false);
    const [showDateTimeModal, setShowDateTimeModal] = useState(false);
    const [selectedDate, setSelectedDate] = useState('');
    const [selectedTime, setSelectedTime] = useState('');
    const maxLength = 500;


    const handleAddTask = (e) => {

      e.preventDefault();
      if (!newTask.trim()) return;

      const dueDate = selectedDate && selectedTime 
      ? `${selectedDate}T${selectedTime}` 
      : null;

      dispatch(addTask({text:newTask,favorite:isFavorite, dueDate: dueDate}));
      setNewTask('');
      setIsFavorite(false);
      setSelectedDate('');
      setSelectedTime('');
      setShowDateTimeModal(false);
      
    };

    const handleOpenDateTimeModal = () => {
      setShowDateTimeModal(true);
    };

   
    useEffect(()=>{
        
        const textarea = textareaRef.current;
        textarea.style.height = 'auto';
        textarea.style.height = `${textarea.scrollHeight}px`;
        const storedTasks = localStorage.getItem('tasks');
        console.log('Stored Tasks:', storedTasks ? JSON.parse(storedTasks) : 'No tasks found');
        const FavTasks = localStorage.getItem('favoritetasks');
        console.log('Stored Tasks:', FavTasks ? JSON.parse(FavTasks) : 'No tasks found');
    },[text]);

    return(
        <>
          <Container className="mx-10 start-0 p-0"
          style={{
            position: 'relative',
            width:"100%",
            height:"300px"
          }}
          >
            
      <Form className="p-0 m-0 start-0">
        <Form.Group>
         
          <Form.Control
            ref={textareaRef}
            as="input"
            value={newTask}
            onChange={(e) => {
                if(e.target.value.length <= maxLength) {
                    setText(e.target.value);
                    setNewTask(e.target.value);
                  }
                }}
            placeholder="Add Task..."
            style={{
              maxHeight: '100px',
              resize: 'none',
              overflow: 'hidden',
              width:"100%",
              position:"absolute",
              top:"30%",
              backgroundColor:"lightgrey"

            }}
          />
         
              
         <div className="d-flex justify-content-between mt-2 end-0 py-2 m-0"  style={{
            position: "absolute",
            top: "40%",
            
          }}>
          <div className="d-flex justify-content-between gap-0 py-0 mx-2 start-0" style={{
            position: "relative"
          }}>
                <Form.Text className="text-muted text-xs px-2" style={{fontSize:"10px"}}>
                  {text.length}/{maxLength} characters
                </Form.Text>
                
                <Button 
                  className="d-flex align-items-center justify-content-center px-2"
                  variant="outline-secondary"
                  onClick={handleOpenDateTimeModal}
                  style={{
                    border:"none",
                  }}
                >
                  <CiCalendarDate />
                </Button>
                <ToggleButton
                key={tasks.id}
                id="toggle-check"
                checked={isFavorite}
                onChange={(e)=>{ 
                  setIsFavorite(!isFavorite);
                }}
                type="checkbox"
                className="p-2
                d-flex 
                align-items-center 
                justify-content-center
                p-3
                "
                style={{
                    height:"30px",
                    alignItems: "center",
                    backgroundColor: "transparent",
                    color: "black",
                    border: "none",
                    transition: "background-color 0.3s ease",
                }}
                onMouseEnter={(e) => {
                  e.target.style.backgroundColor = 'rgba(0,0,0,0.1)'; // Light dark overlay on hover
                }}
                onMouseLeave={(e) => {
                  e.target.style.backgroundColor = 'transparent';
                }}
                >
                  {!isFavorite ? <FaRegStar/> : <FaStar/>}
                

                </ToggleButton>
                </div>
              
                
                <Button 
                  className=" 
                  align-items-center
                  justify-content-center
                  text-align-center
                  "
                  onClick={handleAddTask}
                  variant="outline-secondary" 
                  size="sm"
                  style={{
                    height:"30px",
                    alignItems: "center",
                    backgroundColor: "transparent",
                    color: "black",
                    transition: "background-color 0.3s ease",
                }}
                onMouseEnter={(e) => {
                  e.target.style.backgroundColor = 'rgba(0,0,0,0.1)'; // Light dark overlay on hover
                }}
                onMouseLeave={(e) => {
                  e.target.style.backgroundColor = 'transparent';
                }}
                >
                  Add Task
                </Button>
                
               
              </div>
        </Form.Group>
      </Form>
    </Container>
    <Modal 
        show={showDateTimeModal} 
        onHide={() => setShowDateTimeModal(false)}
      >
        <Modal.Header closeButton>
          <Modal.Title>Set Task Date and Time</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group className="mb-3">
              <Form.Label>Date</Form.Label>
              <Form.Control 
                type="date" 
                value={selectedDate}
                onChange={(e) => setSelectedDate(e.target.value)}
              />
            </Form.Group>
            
            <Form.Group>
              <Form.Label>Time</Form.Label>
              <Form.Control 
                type="time" 
                value={selectedTime}
                onChange={(e) => setSelectedTime(e.target.value)}
              />
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button 
            variant="secondary" 
            onClick={() => setShowDateTimeModal(false)}
          >
            Cancel
          </Button>
          <Button 
            variant="primary" 
            onClick={handleAddTask}
          >
            Set Date and Add Task
          </Button>
        </Modal.Footer>
      </Modal>
        </>
    );
}




function CompletedTasksContainer() {
  const dispatch = useDispatch();
  const { items: tasks } = useSelector(state => state.tasks);

  // Get completed tasks
  const completedTasks = tasks.filter(task => task.completed);

  return (
    <Container className="mt-4">
      <Accordion defaultActiveKey="0">
        <Accordion.Item eventKey="0">
          <Accordion.Header>
            <div className="d-flex align-items-center">
              <FaCheckCircle className="me-2 text-success" />
              Completed Tasks 
              <Badge bg="secondary" className="ms-2">
                {completedTasks.length}
              </Badge>
            </div>
          </Accordion.Header>
          <Accordion.Body>
            {completedTasks.length === 0 ? (
              <div className="text-center text-muted" style={{height:"100px"}}>
                No completed tasks
              </div>
            ) : (
              <ListGroup>
                {completedTasks.map(task => (
                  <ListGroup.Item 
                    key={task.id} 
                    className="d-flex justify-content-between align-items-center"
                  >
                    <div className="d-flex align-items-center">
                      {/* Favorite Star */}
                      <Button 
                        variant="link" 
                        className="p-0 me-2"
                        onClick={() => dispatch(toggleFavorite(task.id))}
                      >
                        {task.favorite ? (
                          <FaStar className="text-warning" />
                        ) : (
                          <FaRegStar className="text-muted" />
                        )}
                      </Button>

                      {/* Task Text */}
                      <span 
                        style={{
                          textDecoration: 'line-through',
                          color: 'gray'
                        }}
                      >
                        {task.text}
                      </span>
                    </div>

                    {/* Task Actions */}
                    <div>
                      {/* Restore Task Button */}
                      <Button 
                        variant="outline-success" 
                        size="sm" 
                        className="me-2"
                        onClick={() => dispatch(toggleTask(task.id))}
                      >
                        Restore
                      </Button>

                      {/* Delete Button */}
                      <Button 
                        variant="danger" 
                        size="sm"
                        onClick={() => dispatch(removeTask(task.id))}
                      >
                        <FaTrash />
                      </Button>
                    </div>
                  </ListGroup.Item>
                ))}
              </ListGroup>
            )}

            {/* Clear All Completed Tasks Button */}
            {completedTasks.length > 0 && (
              <div className="text-center mt-3">
                <Button 
                  variant="outline-danger"
                  onClick={() => dispatch(clearCompleted())}
                >
                  Clear All Completed Tasks
                </Button>
              </div>
            )}
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </Container>
  );
}



function MainContentPage(){
  const dispatch = useDispatch();
  const { items: tasks, filter } = useSelector(state => state.tasks);
  const { isAuthenticated } = useSelector(state => state.auth);
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);

  if (!isAuthenticated) {
    return (
      <Container className="text-center mt-5">
        <h2>Please log in to view your tasks</h2>
      </Container>
    );
  }

  const formatDate = (dateString) => {
    if (!dateString) return 'No due date';
    
    const date = new Date(dateString);
    return date.toLocaleString('en-US', {
      dateStyle: 'medium',
      timeStyle: 'short'
    });
  };

  // Filter tasks based on current filter
  const filteredTasks = tasks.filter(task => {
    switch(filter) {
      case 'active':
        return !task.completed;
      case 'completed':
        return task.completed;
      case 'favorites':
        return task.favorite;
      default:
        return true;
    }
  });
    

    const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const handleFilterChange = (eventKey) => {
    dispatch(setFilter(eventKey));
  };

  const handleTaskClick = (task) => {
    setSelectedTask(task);
    setIsSidebarOpen(true);
  };

    return(
    <>
    <Container fluid style={{
        width:"100%",
        }}
        className="
        start-0
        px-0
        mx-0
        w-100
        "
        >
    <div className="
        start-0
        bg-light          
        px-0
        py-2           
        my-5
        mx-n3            
        border         
        rounded        
        shadow                  
        align-items-center     
        text-tertiary       
        fw-bold
        position-fixed
        
    
    "
    style={{
        width:"100%"
    }}
    
    >
    <Row className="
    g-0
    ">
        {/*MainBar*/}
        <Col xs={12}
        className="
        main-content 
        transition-all 
        duration-300
        py-5
        start-0
        m-0
        
        "

        style={{
            width: isSidebarOpen ? 'calc(100% - 450px)' : '100%',
            transition: 'width 0.3s ease'
          }}

        >
          <AddTask/>
          <Container>
                {/* Filter Dropdown */}
                <div className="d-flex justify-content-between align-items-center mb-3">
                  <Dropdown onSelect={handleFilterChange}>
                    <Dropdown.Toggle 
                      variant="outline-secondary" 
                      id="task-filter-dropdown"
                    >
                      <FaFilter className="me-2" />
                      {filter === 'all' ? 'All Tasks' : 
                       filter === 'active' ? 'Active Tasks' : 
                       filter === 'completed' ? 'Completed Tasks' : 
                       'Favorite Tasks'}
                    </Dropdown.Toggle>

                    <Dropdown.Menu>
                      <Dropdown.Item eventKey="all">All Tasks</Dropdown.Item>
                      <Dropdown.Item eventKey="active">Active Tasks</Dropdown.Item>
                      <Dropdown.Item eventKey="completed">Completed Tasks</Dropdown.Item>
                      <Dropdown.Item eventKey="favorites">Favorite Tasks</Dropdown.Item>
                    </Dropdown.Menu>
                  </Dropdown>

                  {/* Task Count */}
                  <div className="text-muted">
                    {filteredTasks.length} tasks
                  </div>
                </div>
            <ListGroup>
            {
              filteredTasks.length == 0 ?(
                 <ListGroup.Item className="text-center text-muted" style={{height:"200px"}}>
          No tasks to display
        </ListGroup.Item>
              ) : (
                filteredTasks.map(task => (
                  <ListGroup.Item 
                    key={task.id} 
                    className={`d-flex justify-content-between align-items-center ${
                      task.completed ? 'bg-light text-muted' : ''
                    }`}
                    onClick={()=>handleTaskClick(task)}
                  >
                    <div className="d-flex align-items-center">
                      {/* Favorite Toggle */}
                      <Button 
                        variant="link" 
                        className="p-0 me-2"
                        onClick={() =>{ dispatch(toggleFavorite(task.id)); setIsSidebarOpen(false);}}
                      >
                        {task.favorite ? (
                          <FaStar className="text-warning" />
                        ) : (
                          <FaRegStar className="text-muted" />
                        )}
                      </Button>
                       {/* Task Completion Checkbox */}
              <Form.Check 
                type="checkbox"
                className="me-2 border"
                checked={task.completed}
                onChange={() => {dispatch(toggleTask(task.id)); isSidebarOpen(false);}}
              />

              {/* Task Text */}
              <span 
                style={{
                  textDecoration: task.completed ? 'line-through' : 'none',
                }}
              >
                {task.text}
              </span>
            </div>
 {/* Task Actions */}
 <div className="d-flex align-items-center">
  {/* Delete Button */}
  <Button 
                variant="danger" 
                size="sm" 
                className="ms-2"
                onClick={() => {dispatch(removeTask(task.id)); isSidebarOpen(false);}}
              >
                <FaTrash />
              </Button>
            </div>
          </ListGroup.Item>
        ))
      )}
            </ListGroup>
          </Container>
          <CompletedTasksContainer/>
        </Col>

        {/*SideBar*/}
        <Col
        xs = {isSidebarOpen?10:1}
        className={' p-0 m-0 sidebar bg-dark min-vh-100 position-fixed top-0 end-0 transition-all duration-300 z-index-1 align-items-center text-white'}
        style={{width: isSidebarOpen ? '450px' : '0px',
            transition: 'width 0.3s ease'}}
        >
          {selectedTask ? (
            <div className="p-4 w-100">
              <div className="d-flex justify-content-between align-items-center mb-3">
                <h4 className="mb-0">Task Details</h4>
                <Button 
                  variant="link" 
                  className="text-white"
                  onClick={() => setIsSidebarOpen(false)}
                >
                  <IoMdClose size={24} />
                </Button>
              </div>

              <Card className="mb-3">
                <Card.Body>
                  <div className="d-flex justify-content-between align-items-center mb-2">
                    <h5 className="mb-0">{selectedTask.text}</h5>
                    <Button 
                      variant="link"
                      onClick={() => dispatch(toggleFavorite(selectedTask.id))}
                    >
                      {selectedTask.favorite ? (
                        <FaStar className="text-warning" />
                      ) : (
                        <FaRegStar className="text-muted" />
                      )}
                    </Button>
                  </div>

                  <div className="mb-2">
                    <Badge 
                      bg={selectedTask.completed ? 'success' : 'warning'}
                      className="me-2"
                    >
                      {selectedTask.completed ? 'Completed' : 'Active'}
                    </Badge>
                    
                    <Form.Check 
                      type="switch"
                      id="completion-switch"
                      label="Mark as Completed"
                      checked={selectedTask.completed}
                      onChange={() => dispatch(toggleTask(selectedTask.id))}
                    />
                  </div>
                  <div className="mb-2">
                        <strong>Due Date:</strong> {selectedTask.dueDate ? new Date(selectedTask.dueDate).toLocaleString() : 'No due date'}
                      </div>
                      <div className="mb-2">
                        <strong>Reminder Time:</strong> {selectedTask.reminderTime ? new Date(selectedTask.reminderTime).toLocaleString() : 'No reminder set'}
                      </div>


                  <Button 
                    variant="danger" 
                    onClick={() => {
                      dispatch(removeTask(selectedTask.id));
                      setSelectedTask(null);
                      setIsSidebarOpen(false);
                    }}
                  >
                    Delete Task
                  </Button>
                </Card.Body>
              </Card>
            </div>
          ) : (
            <div className="text-center text-white">
              <h5>Select a task to see details</h5>
            </div>
          )}
        </Col>
    </Row>
    
        
    </div>
    </Container>
    
    </>
    );
}

export default MainContentPage;