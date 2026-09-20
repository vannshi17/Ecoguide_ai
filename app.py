import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI
from tavily import TavilyClient


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


# ============================================================
# API CLIENTS
# ============================================================

grok_client = None
tavily_client = None

if XAI_API_KEY:
    grok_client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1"
    )

if TAVILY_API_KEY:
    tavily_client = TavilyClient(
        api_key=TAVILY_API_KEY
    )


# ============================================================
# CUSTOM CSS
# ============================================================

custom_css = """

/* ================================
   GLOBAL
================================ */

body {
    margin: 0;

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(34, 197, 94, 0.13),
            transparent 28%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(16, 185, 129, 0.10),
            transparent 25%
        ),
        #07110d !important;

    color: #ecfdf5 !important;

    font-family:
        Inter,
        ui-sans-serif,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif !important;
}


/* ================================
   MAIN CONTAINER
================================ */

.gradio-container {
    max-width: 1180px !important;
    margin: auto !important;
    padding: 30px 22px 50px !important;
}


/* ================================
   HERO
================================ */

.hero {
    position: relative;
    overflow: hidden;

    border: 1px solid rgba(74, 222, 128, 0.18);
    border-radius: 28px;

    padding: 48px 42px;
    margin-bottom: 24px;

    background:
        linear-gradient(
            135deg,
            rgba(20, 83, 45, 0.55),
            rgba(6, 31, 22, 0.92)
        );

    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.35),
        inset 0 1px rgba(255, 255, 255, 0.04);
}


.hero::before {
    content: "";

    position: absolute;

    width: 280px;
    height: 280px;

    right: -80px;
    top: -100px;

    background: rgba(34, 197, 94, 0.15);

    border-radius: 50%;

    filter: blur(10px);
}


.hero-badge {
    display: inline-block;

    padding: 8px 14px;

    border-radius: 999px;

    background: rgba(34, 197, 94, 0.12);

    border: 1px solid rgba(74, 222, 128, 0.25);

    color: #86efac;

    font-size: 13px;
    font-weight: 700;

    letter-spacing: 0.5px;

    margin-bottom: 18px;
}


.hero h1 {
    margin: 0;

    font-size: clamp(38px, 6vw, 64px);

    line-height: 1;

    letter-spacing: -2px;

    color: #f0fdf4;
}


.hero h1 span {
    color: #4ade80;
}


.hero-subtitle {
    max-width: 680px;

    margin-top: 18px;

    color: #a7f3d0;

    font-size: 17px;

    line-height: 1.7;
}


/* ================================
   STATUS PILLS
================================ */

.status-row {
    display: flex;

    gap: 10px;

    flex-wrap: wrap;

    margin-top: 25px;
}


.status-pill {
    padding: 8px 13px;

    border-radius: 999px;

    background: rgba(255,255,255,0.045);

    border: 1px solid rgba(255,255,255,0.08);

    color: #d1fae5;

    font-size: 12px;
}


/* ================================
   SECTION TITLE
================================ */

.section-title {
    margin: 30px 0 14px;

    color: #ecfdf5;
}


.section-title h2 {
    margin: 0;

    font-size: 24px;
}


.section-title p {
    margin: 6px 0 0;

    color: #86a99a;

    font-size: 14px;
}


/* ================================
   CARDS
================================ */

.input-card,
.output-card,
.info-card {

    border: 1px solid rgba(167, 243, 208, 0.10) !important;

    border-radius: 22px !important;

    background:
        linear-gradient(
            145deg,
            rgba(17, 45, 34, 0.82),
            rgba(8, 25, 18, 0.88)
        ) !important;

    box-shadow:
        0 15px 45px rgba(0, 0, 0, 0.22),
        inset 0 1px rgba(255,255,255,0.025) !important;

    padding: 20px !important;
}


/* ================================
   LABELS
================================ */

label {
    color: #d1fae5 !important;

    font-weight: 700 !important;
}


/* ================================
   INPUT
================================ */

textarea,
input {

    background: rgba(0, 0, 0, 0.22) !important;

    border: 1px solid rgba(134, 239, 172, 0.13) !important;

    color: #f0fdf4 !important;

    border-radius: 15px !important;
}


textarea:focus,
input:focus {

    border-color: rgba(74, 222, 128, 0.65) !important;

    box-shadow:
        0 0 0 3px rgba(34,197,94,0.10) !important;
}


/* ================================
   RADIO BUTTONS
================================ */

.mode-selector {

    background:
        rgba(34, 197, 94, 0.05) !important;

    border:
        1px solid rgba(74, 222, 128, 0.12) !important;

    border-radius:
        16px !important;

    padding:
        14px !important;

    margin-bottom:
        16px !important;
}


/* ================================
   PRIMARY BUTTON
================================ */

.primary-btn {

    border-radius: 14px !important;

    border: none !important;

    background:
        linear-gradient(
            135deg,
            #22c55e,
            #16a34a
        ) !important;

    color: white !important;

    font-weight: 800 !important;

    min-height: 48px !important;

    box-shadow:
        0 10px 25px rgba(34,197,94,0.20) !important;

    transition:
        all 0.2s ease !important;
}


.primary-btn:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 15px 32px rgba(34,197,94,0.32) !important;
}


/* ================================
   CLEAR BUTTON
================================ */

.clear-btn {

    border-radius:
        14px !important;

    min-height:
        48px !important;

    background:
        rgba(255,255,255,0.045) !important;

    border:
        1px solid rgba(255,255,255,0.09) !important;

    color:
        #d1fae5 !important;
}


/* ================================
   OUTPUT BOXES
================================ */

.output-box textarea {

    min-height:
        65px !important;
}


.output-box input,
.output-box textarea {

    border-color:
        rgba(74, 222, 128, 0.10) !important;
}


/* ================================
   STATUS
================================ */

.status-output {

    background:
        rgba(34, 197, 94, 0.06);

    border:
        1px solid rgba(74, 222, 128, 0.12);

    border-radius:
        14px;

    padding:
        8px 12px;

    margin-bottom:
        12px;
}


/* ================================
   EXAMPLES
================================ */

.example-title {

    color:
        #a7f3d0;

    font-weight:
        700;

    margin-top:
        8px;
}


button.secondary {

    border-radius:
        999px !important;
}


/* ================================
   HOW IT WORKS
================================ */

.workflow {

    display:
        grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap:
        12px;

    margin-top:
        15px;
}


.workflow-step {

    padding:
        18px;

    border-radius:
        18px;

    background:
        rgba(255,255,255,0.035);

    border:
        1px solid rgba(255,255,255,0.07);
}


.workflow-icon {

    font-size:
        25px;

    margin-bottom:
        8px;
}


.workflow-step strong {

    display:
        block;

    color:
        #ecfdf5;

    margin-bottom:
        5px;
}


.workflow-step span {

    color:
        #7fa494;

    font-size:
        12px;

    line-height:
        1.5;
}


/* ================================
   FOOTER
================================ */

.footer {

    text-align:
        center;

    margin-top:
        35px;

    padding:
        25px;

    color:
        #668478;

    font-size:
        12px;

    border-top:
        1px solid rgba(255,255,255,0.06);
}


.footer strong {

    color:
        #86efac;
}


/* ================================
   RESPONSIVE
================================ */

@media (max-width: 800px) {

    .hero {

        padding:
            32px 25px;
    }

    .workflow {

        grid-template-columns:
            1fr 1fr;
    }

}


@media (max-width: 520px) {

    .workflow {

        grid-template-columns:
            1fr;
    }

    .hero h1 {

        font-size:
            40px;
    }

}

"""


# ============================================================
# RESPONSE PARSER
# ============================================================

def extract_section(text, marker):

    try:

        start = text.find(marker)

        if start == -1:
            return "Not available"

        start += len(marker)

        remaining = text[start:]

        markers = [
            "CATEGORY:",
            "RECYCLABLE:",
            "DISPOSAL:",
            "REUSE:",
            "SAFETY:",
            "TIP:"
        ]

        positions = []

        for next_marker in markers:

            position = remaining.find(next_marker)

            if position > 0:

                positions.append(position)

        if positions:

            remaining = remaining[
                :min(positions)
            ]

        return remaining.strip()

    except Exception:

        return "Not available"


# ============================================================
# ₹0 DEMO MODE
# ============================================================

def demo_response(waste):

    item = waste.lower()


    # --------------------------------------------------------
    # PLASTIC
    # --------------------------------------------------------

    if (
        "plastic" in item
        or "bottle" in item
    ):

        return (

            "Plastic Waste",

            "Usually Yes",

            "Empty and rinse the bottle, then place it in the appropriate dry-waste or recycling collection.",

            "Reuse it for storage or craft purposes if it is clean and suitable.",

            "Do not burn plastic because it can release harmful fumes.",

            "Prefer reusable bottles and reduce single-use plastic."

        )


    # --------------------------------------------------------
    # PAPER
    # --------------------------------------------------------

    elif (
        "paper" in item
        or "newspaper" in item
        or "cardboard" in item
        or "box" in item
    ):

        return (

            "Paper / Cardboard",

            "Yes",

            "Keep it dry and place it with paper or cardboard recycling.",

            "Reuse boxes for storage or packing.",

            "Do not mix heavily wet or contaminated paper with recyclable paper.",

            "Recycling paper helps reduce the demand for fresh raw materials."

        )


    # --------------------------------------------------------
    # GLASS
    # --------------------------------------------------------

    elif (
        "glass" in item
        or "jar" in item
    ):

        return (

            "Glass",

            "Usually Yes",

            "Rinse the container and place it in a suitable glass-recycling collection.",

            "Reuse the jar as a storage container.",

            "Handle broken glass carefully and keep it separate from normal waste.",

            "Glass can often be recycled repeatedly."

        )


    # --------------------------------------------------------
    # FOOD / ORGANIC
    # --------------------------------------------------------

    elif (
        "banana" in item
        or "food" in item
        or "vegetable" in item
        or "fruit" in item
        or "peel" in item
    ):

        return (

            "Organic / Food Waste",

            "Compostable",

            "Place suitable food waste in a composting or organic-waste collection.",

            "Use suitable food scraps for composting.",

            "Avoid mixing food waste with dry recyclable materials.",

            "Composting organic waste can help return nutrients to the soil."

        )


    # --------------------------------------------------------
    # BATTERY
    # --------------------------------------------------------

    elif (
        "battery" in item
        or "lithium" in item
        or "cell" in item
    ):

        return (

            "Electronic / Hazardous Waste",

            "Special Collection",

            "Take batteries to an authorized battery or e-waste collection point.",

            "Do not attempt to open or modify the battery.",

            "Keep damaged batteries away from heat and regular household waste.",

            "Proper battery recycling helps recover valuable materials safely."

        )


    # --------------------------------------------------------
    # ELECTRONICS
    # --------------------------------------------------------

    elif (
        "mobile" in item
        or "phone" in item
        or "laptop" in item
        or "computer" in item
        or "electronic" in item
        or "charger" in item
    ):

        return (

            "Electronic Waste",

            "Special Collection",

            "Take the device to an authorized e-waste collection or recycling center.",

            "If working, consider donating or repairing it.",

            "Do not dismantle electronic devices yourself.",

            "Responsible e-waste recycling helps recover useful materials."

        )


    # --------------------------------------------------------
    # GENERAL WASTE
    # --------------------------------------------------------

    else:

        return (

            "General Waste",

            "Depends on Material",

            "Separate the item according to its material and use the appropriate waste collection.",

            "Consider whether the item can be reused, repaired or donated.",

            "Do not mix unknown or potentially hazardous waste with normal waste.",

            "Proper waste segregation makes recycling more effective."

        )


# ============================================================
# AI RECYCLING AGENT
# ============================================================

def analyze_waste(waste, mode):

    if not waste or not waste.strip():

        return (

            "Please enter a waste item.",
            "",
            "",
            "",
            "",
            "",
            "⚪ Waiting for input"

        )


    waste = waste.strip()


    # ========================================================
    # ₹0 DEMO MODE
    # ========================================================

    if mode == "₹0 Demo Mode":

        print("\n" + "=" * 60)
        print("🟢 DEMO MODE")
        print("=" * 60)

        print(
            "Waste:",
            waste
        )

        print(
            "No Grok API request was made."
        )

        print("=" * 60 + "\n")


        result = demo_response(waste)


        return (

            *result,

            "🟢 ₹0 Demo Mode • No Grok API credits used"

        )


    # ========================================================
    # LIVE GROK MODE
    # ========================================================

    if mode == "🔵 Live Grok Mode":


        # ----------------------------------------------------
        # CHECK GROK
        # ----------------------------------------------------

        if not grok_client:

            result = demo_response(waste)

            return (

                *result,

                "🟡 Grok API key missing • Showing ₹0 Demo Mode"

            )


        # ----------------------------------------------------
        # TAVILY SEARCH
        # ----------------------------------------------------

        web_information = ""


        if tavily_client:

            try:

                search_query = (
                    f"how to recycle or dispose of {waste}"
                )


                search_results = tavily_client.search(

                    query=search_query,

                    max_results=3

                )


                for result in search_results.get(
                    "results",
                    []
                ):

                    title = result.get(
                        "title",
                        ""
                    )

                    content = result.get(
                        "content",
                        ""
                    )


                    web_information += (

                        f"\nSource: {title}\n"

                        f"Information: {content}\n"

                    )


            except Exception as e:

                print(
                    "Tavily Error:",
                    e
                )


        # ----------------------------------------------------
        # GROK PROMPT
        # ----------------------------------------------------

        prompt = f"""

You are EcoGuide AI, an AI recycling recommendation assistant.

Waste item:

{waste}

Give a simple, practical and environmentally responsible
recommendation.

Use the following web information when useful:

{web_information}

Return EXACTLY these six sections:

CATEGORY:
<category>

RECYCLABLE:
<Yes, No, or Depends>

DISPOSAL:
<recommended disposal method>

REUSE:
<one possible reuse idea>

SAFETY:
<short safety note>

TIP:
<short environmental tip>

Keep the answer concise and suitable for a college
mini project demonstration.

For batteries, electronics or potentially hazardous items,
provide only general safe disposal guidance.
"""


        # ----------------------------------------------------
        # GROK REQUEST
        # ----------------------------------------------------

        try:

            print("\n" + "=" * 60)

            print(
                "🔵 LIVE GROK MODE"
            )

            print("=" * 60)

            print(
                "Sending request to Grok..."
            )

            print("=" * 60)


            response = grok_client.chat.completions.create(

                model="grok-4.1-fast",

                messages=[

                    {

                        "role": "system",

                        "content":
                            "You are EcoGuide AI, "
                            "a helpful recycling assistant."

                    },

                    {

                        "role": "user",

                        "content": prompt

                    }

                ],

                temperature=0.2

            )


            answer = response.choices[0].message.content


            print("\nGROK RESPONSE")

            print("-" * 60)

            print(answer)

            print("-" * 60 + "\n")


            return (

                extract_section(
                    answer,
                    "CATEGORY:"
                ),

                extract_section(
                    answer,
                    "RECYCLABLE:"
                ),

                extract_section(
                    answer,
                    "DISPOSAL:"
                ),

                extract_section(
                    answer,
                    "REUSE:"
                ),

                extract_section(
                    answer,
                    "SAFETY:"
                ),

                extract_section(
                    answer,
                    "TIP:"
                ),

                "🔵 Live Grok Mode • Tavily research enabled"

            )


        # ====================================================
        # AUTOMATIC DEMO FALLBACK
        # ====================================================

        except Exception as e:

            print("\n" + "=" * 60)

            print(
                "⚠️ GROK API UNAVAILABLE"
            )

            print("=" * 60)

            print(e)

            print("=" * 60)

            print(
                "Switching to ₹0 Demo Mode..."
            )

            print("=" * 60 + "\n")


            result = demo_response(waste)


            return (

                *result,

                "🟡 Grok unavailable • Automatically using ₹0 Demo Mode"

            )


    # ========================================================
    # UNKNOWN MODE
    # ========================================================

    result = demo_response(waste)


    return (

        *result,

        "🟢 ₹0 Demo Mode"

    )


# ============================================================
# CLEAR
# ============================================================

def clear_all():

    return (

        "",

        "",

        "",

        "",

        "",

        "",

        "⚪ Waiting for input"

    )


# ============================================================
# GRADIO APP
# ============================================================

with gr.Blocks(
    title="EcoGuide AI"
) as demo:


    # ========================================================
    # HERO
    # ========================================================

    gr.HTML(
        """

        <div class="hero">

            <div class="hero-badge">
                ♻️ AGENTIC AI • ECO TECHNOLOGY
            </div>


            <h1>
                EcoGuide <span>AI</span>
            </h1>


            <div class="hero-subtitle">

                Make smarter waste decisions with AI.

                Describe a waste item and get an intelligent
                recommendation for recycling, disposal and reuse.

            </div>


            <div class="status-row">

                <div class="status-pill">
                    🤖 Grok AI
                </div>

                <div class="status-pill">
                    🔎 Tavily Search
                </div>

                <div class="status-pill">
                    ⚡ Gradio
                </div>

                <div class="status-pill">
                    🌱 Sustainability
                </div>

            </div>

        </div>

        """
    )


    # ========================================================
    # MAIN SECTION TITLE
    # ========================================================

    gr.HTML(
        """

        <div class="section-title">

            <h2>
                What are you throwing away?
            </h2>

            <p>
                Enter an item below and let EcoGuide analyze it.
            </p>

        </div>

        """
    )


    # ========================================================
    # MAIN COLUMNS
    # ========================================================

    with gr.Row():


        # ====================================================
        # INPUT CARD
        # ====================================================

        with gr.Column(
            elem_classes="input-card"
        ):


            gr.Markdown(
                """

                ### 🗑️ Waste Input

                Describe the item you want to dispose of.

                """
            )


            # ------------------------------------------------
            # MODE SELECTOR
            # ------------------------------------------------

            mode_selector = gr.Radio(

                choices=[

                    "₹0 Demo Mode",

                    "🔵 Live Grok Mode"

                ],

                value="₹0 Demo Mode",

                label="🤖 AI Mode",

                info=(
                    "Demo Mode is completely free. "
                    "Live Grok Mode uses your xAI API credits."
                ),

                elem_classes="mode-selector"

            )


            # ------------------------------------------------
            # WASTE INPUT
            # ------------------------------------------------

            waste_input = gr.Textbox(

                label="Waste item",

                placeholder=(
                    "Example: plastic water bottle"
                ),

                lines=5

            )


            # ------------------------------------------------
            # BUTTONS
            # ------------------------------------------------

            with gr.Row():


                analyze_button = gr.Button(

                    "🔍 Analyze Waste",

                    variant="primary",

                    elem_classes="primary-btn"

                )


                clear_button = gr.Button(

                    "↻ Clear",

                    elem_classes="clear-btn"

                )


            gr.Markdown(
                """

                **Tip:** Be specific for a more useful recommendation.

                """
            )


        # ====================================================
        # OUTPUT CARD
        # ====================================================

        with gr.Column(
            elem_classes="output-card"
        ):


            gr.Markdown(
                """

                ### 🧠 AI Recommendation

                Your personalized recycling guide will appear here.

                """
            )


            # ------------------------------------------------
            # MODE STATUS
            # ------------------------------------------------

            mode_status = gr.Markdown(

                "⚪ Waiting for input",

                elem_classes="status-output"

            )


            # ------------------------------------------------
            # OUTPUTS
            # ------------------------------------------------

            category_output = gr.Textbox(

                label="📦 Waste Category",

                elem_classes="output-box"

            )


            recyclable_output = gr.Textbox(

                label="♻️ Recycling Status",

                elem_classes="output-box"

            )


            disposal_output = gr.Textbox(

                label="🚮 Recommended Disposal",

                lines=2,

                elem_classes="output-box"

            )


            reuse_output = gr.Textbox(

                label="🔄 Reuse Option",

                lines=2,

                elem_classes="output-box"

            )


            safety_output = gr.Textbox(

                label="⚠️ Safety Note",

                lines=2,

                elem_classes="output-box"

            )


            tip_output = gr.Textbox(

                label="🌱 Environmental Tip",

                lines=2,

                elem_classes="output-box"

            )


    # ========================================================
    # EXAMPLES
    # ========================================================

    gr.HTML(
        """

        <div class="section-title">

            <h2>
                💡 Try an example
            </h2>

            <p>
                Click any example to automatically fill the input.
            </p>

        </div>

        """
    )


    gr.Examples(

        examples=[

            ["Plastic water bottle"],

            ["Old mobile phone"],

            ["Used lithium battery"],

            ["Newspaper"],

            ["Banana peel"],

            ["Glass jar"],

            ["Cardboard packaging box"]

        ],

        inputs=waste_input

    )


    # ========================================================
    # WORKFLOW
    # ========================================================

    gr.HTML(
        """

        <div class="section-title">

            <h2>
                ⚙️ How EcoGuide works
            </h2>

            <p>
                A simple AI-assisted workflow for smarter recycling.
            </p>

        </div>


        <div class="workflow">


            <div class="workflow-step">

                <div class="workflow-icon">
                    📝
                </div>

                <strong>
                    01 · Describe
                </strong>

                <span>
                    Enter the waste item you want to analyze.
                </span>

            </div>


            <div class="workflow-step">

                <div class="workflow-icon">
                    🔎
                </div>

                <strong>
                    02 · Research
                </strong>

                <span>
                    Tavily can retrieve relevant recycling information.
                </span>

            </div>


            <div class="workflow-step">

                <div class="workflow-icon">
                    🤖
                </div>

                <strong>
                    03 · Reason
                </strong>

                <span>
                    Grok analyzes the item and generates a recommendation.
                </span>

            </div>


            <div class="workflow-step">

                <div class="workflow-icon">
                    🌱
                </div>

                <strong>
                    04 · Act
                </strong>

                <span>
                    Get practical guidance for recycling, disposal and reuse.
                </span>

            </div>


        </div>

        """
    )


    # ========================================================
    # BUTTON EVENTS
    # ========================================================

    analyze_button.click(

        fn=analyze_waste,

        inputs=[

            waste_input,

            mode_selector

        ],

        outputs=[

            category_output,

            recyclable_output,

            disposal_output,

            reuse_output,

            safety_output,

            tip_output,

            mode_status

        ]

    )


    # ========================================================
    # CLEAR BUTTON
    # ========================================================

    clear_button.click(

        fn=clear_all,

        inputs=[],

        outputs=[

            waste_input,

            category_output,

            recyclable_output,

            disposal_output,

            reuse_output,

            safety_output,

            tip_output,

            mode_status

        ]

    )


    # ========================================================
    # FOOTER
    # ========================================================

    gr.HTML(
        """

        <div class="footer">

            <strong>
                ♻️ EcoGuide AI
            </strong>

            <br>

            AI-Powered Recycling Recommendation Assistant

            <br><br>

            Built with
            <strong>Grok</strong> •
            <strong>Tavily</strong> •
            <strong>Gradio</strong>

            <br><br>

            Supports
            <strong>Live AI</strong> +
            <strong>₹0 Demo Mode</strong>

            <br><br>

            🌍 Small decisions. Smarter recycling. A cleaner future.

        </div>

        """
    )


# ============================================================
# LAUNCH
# ============================================================

if __name__ == "__main__":

    print("\n")

    print("=" * 60)

    print("♻️  ECOGUIDE AI")

    print("=" * 60)


    print(

        "Grok API Key:",

        "Loaded ✅"
        if XAI_API_KEY
        else
        "Missing ❌"

    )


    print(

        "Tavily API Key:",

        "Loaded ✅"
        if TAVILY_API_KEY
        else
        "Missing ❌"

    )


    print("=" * 60)

    print(
        "Starting EcoGuide AI Gradio Server..."
    )

    print("=" * 60)

    print("\n")


    demo.launch(

        css=custom_css

    )