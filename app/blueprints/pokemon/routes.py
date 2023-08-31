from ...models import db
from . import pokemon


# @pokemon.route("/questionnaire", methods=["GET", "POST"])
# def questionnaire():
#     questions = [
#         "Username",
#         "Select a team",
#         "Select an initial Pokemon",
#     ]
#     current_question = int(request.form.get("current_question", 0))
#
#     form = InitialDataForm()
#
#     if request.method == "POST":
#         current_question += 1
#         if current_question < len(questions):
#             question_field_name = f"question_{current_question}"
#             setattr(form, question_field_name, request.form[question_field_name])
#         else:
#             # All questions answered, process the form data
#             if form.validate_on_submit():
#                 initial_data = InitialData(
#                     user_id=0,  # Replace with the actual user ID
#                     level=1,  # Replace with the desired level
#                     xp=0,  # Replace with the initial XP value
#                     items={},  # Replace with the initial items
#                     pokemon={},  # Replace with the initial pokemon
#                     team=form.team.data,
#                     user_idel=form.user_idel.data,
#                     user_idmove="default",  # Replace with the desired value
#                 )
#                 db.session.add(initial_data)
#                 db.session.commit()
#                 return redirect(url_for("thank_you"))
#
#     question_field_name = f"question_{current_question}"
#     return render_template(
#         "questionnaire.html",
#         form=form,
#         questions=questions,
#         current_question=current_question,
#         question_field_name=question_field_name,
#     )


# # app/pokemon/routes.py
# from flask import request, redirect, url_for, render_template
#
# from app.models import InitialData, db
# from . import pokemon
# from .forms import InitialDataForm
#
#
# @pokemon.route("/questionnaire", methods=["GET", "POST"])
# def questionnaire():
#     questions = [
#         "Username",
#         "Select a team",
#         "Select an initial Pokemon",
#     ]
#     current_question = int(request.form.get("current_question", 0))
#
#     form = InitialDataForm()
#
#     if request.method == "POST":
#         current_question += 1
#         if current_question < len(questions):
#             question_field_name = f"question_{current_question}"
#             setattr(form, question_field_name, request.form[question_field_name])
#         else:
#             # All questions answered, process the form data
#             if form.validate_on_submit():
#                 initial_data = InitialData(
#                     user_idel=form.user_idel.data,
#                     team=form.team.data,
#                     pokemon=form.pokemon.data,
#                 )
#                 db.session.add(initial_data)
#                 db.session.commit()
#                 return redirect(url_for("pokemon.thank_you"))
#
#     question_field_name = f"question_{current_question}"
#     return render_template(
#         "questionnaire.html",
#         form=form,
#         questions=questions,
#         current_question=current_question,
#         question_field_name=question_field_name,
#     )


# from flask import request, redirect, url_for, render_template
#
# from app.models import InitialData, db
# from . import pokemon
# from .forms import InitialDataForm
#
#
# @pokemon.route("/questionnaire", methods=["GET", "POST"])
# def questionnaire():
#     questions = [
#         "Username",
#         "Select a team",
#         "Select an initial Pokemon",
#     ]
#     current_question = int(request.form.get("current_question", 1))
#
#     form = InitialDataForm()
#
#     if request.method == "POST":
#         current_question += 1
#         if current_question < len(questions):
#             question_field_name = f"question_{current_question}"
#             setattr(form, question_field_name, request.form[question_field_name])
#         else:
#             # All questions answered, process the form data
#             initial_data = InitialData(
#                 user_idel=form.user_idel.data,
#                 team=form.team.data,
#                 pokemon=form.pokemon.data,
#             )
#             db.session.add(initial_data)
#             db.session.commit()
#             return redirect(url_for("pokemon.thank_you"))
#
#     return render_template(
#         "questionnaire.html",
#         form=form,
#         questions=questions,
#         current_question=current_question,
#     )


#
# @pokemon.route("/pokemon", methods=["GET", "POST"])
# def pokemon():
#     card = Pokemonclass.get_card_by_name("Pikachu")  # Replace "Pikachu" with user input
#     img_url = card.get("images", {}).get(
#         "small"
#     )  # Adjust based on the actual API response
#     return render_template("pokemon.html", img_url=img_url)


# @pokemon.route("/questionnaire", methods=["GET", "POST"])
# def questionnaire():
#     questions = [
#         "Username",
#         "Select a team",
#         "Select an initial Pokemon",
#     ]
#     current_question = int(request.form.get("current_question", 0))
#
#     form = InitialDataForm()
#
#     if request.method == "POST":
#         current_question += 1
#         if current_question < len(questions):
#             question = questions[current_question]
#             setattr(form, f"question_{current_question}", request.form[question])
#         else:
#             # All questions answered, process the form data
#             initial_data = InitialData(
#                 team=form.team.data,
#                 user_idel=form.user_idel.data,
#                 pokemon=form.pokemon.data,
#                 # user_idmove=form.user_idmove.data,
#                 # level=form.level.data,
#                 # xp=form.xp.data,
#                 # items=form.items.data,
#             )
#             db.session.add(initial_data)
#             db.session.commit()
#             return redirect(url_for("pokemon.thank_you"))
#
#     return render_template(
#         "questionnaire.html",
#         form=form,
#         questions=questions,
#         current_question=current_question,
#     )


@pokemon.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


# @pokemon.route("/questionnaire", methods=["GET", "POST"])
# def questionnaire():
#     form = QuestionnaireForm()
#
#     if form.validate_on_submit():
#         submission = Submission(name=form.name.data, gender=form.gender.data)
#         db.session.add(submission)
#         db.session.commit()
#         return "Form submitted successfully!"
#
#     return render_template("questionnaire.html", form=form)


from flask import render_template
from .forms import InitialDataForm  # Replace 'your_forms' with the actual import
from ...models import InitialData
from flask_login import current_user

@pokemon.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():
    form = InitialDataForm()

    if form.validate_on_submit():
        user_id = current_user.id
        new_data = InitialData(
            user_id=user_id,  # This should be replaced with the actual user ID.
            level=1,  # This should be replaced with the actual level.
            xp=0,  # This should be replaced with the actual xp.
            items={},  # This should be replaced with the actual items.
            pokemon=form.pokemon.data,
            team=form.team.data,
            user_idel=form.user_idel.data,
            user_idmove="",  # This should be replaced with the actual user_idmove.
        )
        db.session.add(new_data)
        db.session.commit()

        user_id = current_user.id

    # Get the user's team from InitialData
        initial_data = InitialData.query.filter_by(user_id=user_id).first()
        print(initial_data.team)

        return "Form submitted successfully!"

    return render_template("questionnaire.html", form=form)
