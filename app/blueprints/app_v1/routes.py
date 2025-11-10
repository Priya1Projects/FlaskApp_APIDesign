from  flask import Blueprint, jsonify,request,current_app  
from app.services import SummarizerService, SummarizeResult
from app.schemas import SummarizeRequestSchema
bp= Blueprint('app_v1', __name__)

@bp.route("/")
def home():
    return "Welcome to the Home Page!"

@bp.route("/get-user/<user_id>")
def get_user(user_id):
        # Simulated user data
        users= {
            "name": "Alice", "age": 30, "id": "1",
            "name": "Bob", "age": 25, "id": "2"
        }
        user= users.get(user_id)
        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "User not found"}), 404

@bp.route("/generate-summary", methods=["POST"])
def generate_summary():
    data = request.get_json(silent=False)

    # Validate input
    model, errors = SummarizeRequestSchema.validate(**data)
    if errors:
        return jsonify({"error": errors}), 400
    # Simulate summary generation
    summary = current_app.extensions['summarizer'].summarize_text(
        text=model.text, max_length=model.max_length
    )
    return jsonify(summary)