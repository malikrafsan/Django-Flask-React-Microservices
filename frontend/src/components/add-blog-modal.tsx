import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";
import { useState } from "react";
import axios from "axios";

export const AddBlogModal = (props: {
  show: boolean;
  handleClose: () => void;
}) => {
  const { show, handleClose } = props;

  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const clearInput = () => {
    setTitle("");
    setContent("");
  }

  const handleSave = async () => {
    console.log(title, content);
    const { data } = await axios.post(
      "http://localhost:8000/blog/",
      {
        title,
        content,
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
        withCredentials: true,
      }
    )
    console.log(data);

    clearInput();
    handleClose();
  };

  return (
    <Modal show={show} onHide={handleClose}>
      <Form>
        <Modal.Header closeButton>
          <Modal.Title>Add Blog</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form.Group className="mb-3">
            <Form.Label>Title</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter blog title"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Content</Form.Label>
            <Form.Control
              type="textarea"
              placeholder="Enter blog content"
              value={content}
              onChange={(e) => setContent(e.target.value)}
            />
          </Form.Group>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="primary" onClick={handleSave}>
            Save
          </Button>
        </Modal.Footer>
      </Form>
    </Modal>
  );
};
