from flask_socketio import SocketIO

# SocketIO instance - message_queue is configured in create_app based on environment
socketio = SocketIO(cors_allowed_origins="*")

def emit_ranking_update(job_id: int):
    """
    Emits an event to the specific job's room when rankings are recalculated.
    """
    socketio.emit(
        'ranking_updated',
        {'job_id': job_id, 'message': 'Candidate rankings have been updated'},
        room=f"job_{job_id}"
    )

def emit_notification(user_id: int, message: str):
    """
    Emits a direct notification to a user.
    """
    socketio.emit(
        'notification',
        {'message': message},
        room=f"user_{user_id}"
    )
