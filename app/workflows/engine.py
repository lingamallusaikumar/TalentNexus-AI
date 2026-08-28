from app.workflows.models import WorkflowRule, WorkflowExecution
from app.extensions import db
import logging

logger = logging.getLogger(__name__)

def evaluate_conditions(conditions: list, context: dict) -> bool:
    """
    Evaluates a list of conditions against a context dict.
    context = {"score": 90, "stage": "Applied"}
    conditions = [{"field": "score", "operator": ">=", "value": 85}]
    """
    for cond in conditions:
        field = cond.get('field')
        op = cond.get('operator')
        value = cond.get('value')
        
        context_val = context.get(field)
        if context_val is None:
            return False
            
        if op == '==':
            if not context_val == value: return False
        elif op == '>=':
            if not context_val >= value: return False
        elif op == '<=':
            if not context_val <= value: return False
        elif op == '>':
            if not context_val > value: return False
        elif op == '<':
            if not context_val < value: return False
        else:
            logger.warning(f"Unknown operator {op}")
            return False
            
    return True

def execute_action(action: dict, target_entity_id: int, target_entity_type: str):
    """
    Executes the configured action.
    """
    action_type = action.get('type')
    
    if action_type == 'move_stage' and target_entity_type == 'Application':
        target_stage = action.get('target')
        from app.applications.models import Application, ApplicationHistory
        app = Application.query.get(target_entity_id)
        if app and app.current_stage != target_stage:
            old_stage = app.current_stage
            app.current_stage = target_stage
            
            history = ApplicationHistory(
                application_id=app.id,
                from_stage=old_stage,
                to_stage=target_stage,
                notes="Automated by Workflow Engine"
            )
            db.session.add(history)
            
    elif action_type == 'notify':
        pass # To be integrated with Notifications
    else:
        logger.warning(f"Unknown action type: {action_type}")

def process_event(organization_id: int, trigger_event: str, target_entity_type: str, target_entity_id: int, context: dict):
    """
    Entrypoint for emitting events to the workflow engine.
    """
    rules = WorkflowRule.query.filter_by(
        organization_id=organization_id, 
        trigger_event=trigger_event,
        is_active=True
    ).all()
    
    for rule in rules:
        try:
            if evaluate_conditions(rule.conditions, context):
                for action in rule.actions:
                    execute_action(action, target_entity_id, target_entity_type)
                
                execution = WorkflowExecution(
                    rule_id=rule.id,
                    target_entity_id=target_entity_id,
                    target_entity_type=target_entity_type,
                    status='Success'
                )
                db.session.add(execution)
        except Exception as e:
            logger.error(f"Workflow {rule.id} failed: {str(e)}")
            execution = WorkflowExecution(
                rule_id=rule.id,
                target_entity_id=target_entity_id,
                target_entity_type=target_entity_type,
                status='Failed',
                error_message=str(e)
            )
            db.session.add(execution)
            
    db.session.commit()
