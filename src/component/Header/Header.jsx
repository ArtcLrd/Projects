import React, { useState,useEffect } from "react";
import {
  Button,
  Container,
  Navbar,
  Offcanvas,
  Nav,
  Modal,
  Form
} from "react-bootstrap";
import { IoMenuSharp } from "react-icons/io5";
import { IoMdClose } from "react-icons/io";
import { useDispatch, useSelector } from "react-redux";
import { login, logout } from "../Slices/AuthSlice";
import "bootstrap/dist/css/bootstrap.min.css";

function Header() {
  const dispatch = useDispatch();
  const [showLoginModal, setShowLoginModal] = useState(false);
  const { isAuthenticated, user } = useSelector(state => state.auth);
  const [showPanel, setShowPanel] = useState(false);
  const handlePanelToggle = () => {
    setShowPanel(!showPanel);
  };

  const [loginCredentials, setLoginCredentials] = useState({
    username: "",
    password: "",
  });
  const handleLoginModalOpen = () => {
    setShowLoginModal(true);
  };
  const handleLogin = (e) => {
    e.preventDefault();

   
    if (loginCredentials.username && loginCredentials.password) {
      
      dispatch(
        login({
          username: loginCredentials.username,
          
        })
      );

     
      setShowLoginModal(false);
      setShowPanel(false);
    } else {
    
      alert("Please enter username and password");
    }
  };
  const handleLogout = () => {
    dispatch(logout());
    setShowPanel(false);
  };


  return (
    <>
      <Navbar bg="light" expand="sm" className="py-2 shadow-sm" fixed="top">
        <Container fluid className="px-4">
          <div
            className="
             d-flex 
             align-items-center 
             gap-2
           "
          >
            <Button
              className="py-3
            d-flex 
            align-items-center 
            justify-content-center"
              onClick={handlePanelToggle}
              style={{
                height: "50px",
                alignItems: "center",
                backgroundColor: "transparent",
                color: "black",
                border: "none",
              }}
            >
              {!showPanel ? <IoMenuSharp /> : <IoMdClose />}
            </Button>
            <Navbar.Brand
              href="#home"
              className="px-2 d-flex align-items-center"
            >
              DoIt
            </Navbar.Brand>
          </div>
          <div
            className="
             d-flex 
             align-items-center 
             gap-3"
          >
          </div>
        </Container>
      </Navbar>

      <Offcanvas
        show={showPanel}
        onHide={() => setShowPanel(false)}
        placement="start"
      >
        <Offcanvas.Header
          closeButton
          className="  justify-content-center align-content-center px-4 py-3"
        >
          <Offcanvas.Title className="justify-content-center align-items-center text-md-center">
            Profile
          </Offcanvas.Title>
        </Offcanvas.Header>
        <div className="px-4 mb-3">
                    {!isAuthenticated ? (
                        <Button 
                            variant="primary" 
                            className="w-100"
                            onClick={handleLoginModalOpen}
                        >
                            Login
                        </Button>
                    ) : (
                        <Button 
                            variant="danger" 
                            className="w-100"
                            onClick={handleLogout}
                        >
                            Logout
                        </Button>
                    )}
                </div>
        <Offcanvas.Body>
          <Nav className="flex-column"></Nav>

          {/* User Profile Section */}
          {isAuthenticated && (
                        <div className="mt-auto">
                            <hr />
                            <div className="d-flex align-items-center offset-4 py-1">
                                <img
                                    src="/vite.svg"
                                    alt="User Avatar"
                                    className="rounded-circle me-2"
                                    style={{ width: '100px', height: '100px' }}
                                />
                                <div className="" style={{position: "absolute", top:"300px"}}>
                                    <strong>{user?.username || 'User'}</strong>
                                    <div className="text-muted">{user?.email || 'user@example.com'}</div>
                                </div>
                            </div>
                        </div>
                    )}

        </Offcanvas.Body>
      </Offcanvas>
       {/* Login Modal */}
       <Modal 
                show={showLoginModal} 
                onHide={() => setShowLoginModal(false)}
                centered
            >
                <Modal.Header closeButton>
                    <Modal.Title>Login</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form onSubmit={handleLogin}>
                        <Form.Group className="mb-3">
                            <Form.Label>Username</Form.Label>
                            <Form.Control 
                                type="text" 
                                placeholder="Enter username"
                                value={loginCredentials.username}
                                onChange={(e) => setLoginCredentials(prev => ({
                                    ...prev,
                                    username: e.target.value
                                }))}
                                required
                            />
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label>Password</Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Password"
                                value={loginCredentials.password}
                                onChange={(e) => setLoginCredentials(prev => ({
                                    ...prev,
                                    password: e.target.value
                                }))}
                                required
                            />
                        </Form.Group>

                        <Button variant="primary" type="submit" className="w-100">
                            Login
                        </Button>
                    </Form>
                </Modal.Body>
            </Modal>
    </>
  );
}

export default Header;
