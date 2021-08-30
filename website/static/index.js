
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function goToShelf(shelf_id) {
  fetch("/shelf", {
    method: "POST",
    body: JSON.stringify({ shelf_id: shelf_id }),
  }).then((_res) => {
    window.location.href = "/shelf";
  });
}